import ubelt as ub


class DuplicateJobError(KeyError):
    ...


class UnknownBackendError(KeyError):
    ...


class Job(ub.NiceRepr):
    """
    Base class for a job
    """
    def __init__(self, command=None, name=None, depends=None, **kwargs):
        # This is unused, should the slurm and bash job reuse this?
        if depends is not None and not ub.iterable(depends):
            depends = [depends]
        self.name = name
        self.command = command
        self.depends = depends
        self.kwargs = kwargs

    def __nice__(self):
        return self.name


class Queue(ub.NiceRepr):
    """
    Base class for a queue.

    Use the ``create`` classmethod to make a concrete instance with an
    available backend.
    """

    def __init__(self):
        self.num_real_jobs = 0
        self.all_depends = None
        self.named_jobs = {}

    def change_backend(self, backend, **kwargs):
        """
        Create a new version of this queue with a different backend.

        Currently metadata is not carried over. Submit an MR if you need this
        functionality.

        Example:
            >>> from cmd_queue import Queue
            >>> self = Queue.create(size=5, name='demo')
            >>> self.submit('echo "Hello World"', name='job1a')
            >>> self.submit('echo "Hello Revocable"', name='job1b')
            >>> self.submit('echo "Hello Crushed"', depends=['job1a'], name='job2a')
            >>> self.submit('echo "Hello Shadow"', depends=['job1b'], name='job2b')
            >>> self.submit('echo "Hello Excavate"', depends=['job2a', 'job2b'], name='job3')
            >>> self.submit('echo "Hello Barrette"', depends=[], name='jobX')
            >>> self.submit('echo "Hello Overwrite"', depends=['jobX'], name='jobY')
            >>> self.submit('echo "Hello Giblet"', depends=['jobY'], name='jobZ')
            >>> serial_backend = self.change_backend('serial')
            >>> tmux_backend = self.change_backend('tmux')
            >>> slurm_backend = self.change_backend('slurm')
            >>> airflow_backend = self.change_backend('airflow')
            >>> serial_backend.print_commands()
            >>> tmux_backend.print_commands()
            >>> slurm_backend.print_commands()
            >>> airflow_backend.print_commands()
        """
        new = Queue.create(backend=backend, **kwargs)
        for job_name, job in self.named_jobs.items():
            new_depends = []
            if job.depends:
                for dep in job.depends:
                    new_dep = new.named_jobs[dep.name]
                    new_depends.append(new_dep)
            # TODO: carry over metadata
            new.submit(job.command, depends=new_depends, name=job.name)
        return new

        for job in self.jobs:
            new.submit(job.commands)
            pass

    def __len__(self):
        return self.num_real_jobs

    def sync(self):
        """
        Mark that all future jobs will depend on the current sink jobs

        Returns:
            Queue:
                a reference to the queue (for chaining)
        """
        graph = self._dependency_graph()
        # Find the jobs that nobody depends on
        sink_jobs = [graph.nodes[n]['job'] for n, d in graph.out_degree if d == 0]
        # All new jobs must depend on these jobs
        self.all_depends = sink_jobs
        return self

    def write(self):
        """
        Writes the underlying files that defines the queue for whatever program
        will ingest it to run it.
        """
        import os
        import stat
        text = self.finalize_text()
        self.fpath.parent.ensuredir()
        self.fpath.write_text(text)
        os.chmod(self.fpath, (
            stat.S_IXUSR | stat.S_IXGRP | stat.S_IRUSR |
            stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP))
        return self.fpath

    def submit(self, command, **kwargs):
        """
        Args:
            name: specify the name of the job
            **kwargs: passed to :class:`cmd_queue.serial_queue.BashJob`
        """
        # TODO: we could accept additional args here that modify how we handle
        # the command in the bash script we build (i.e. if the script is
        # allowed to fail or not)
        # self.commands.append(command)
        # hack
        from cmd_queue import serial_queue

        if 'info_dpath' not in kwargs:
            kwargs['info_dpath'] = self.job_info_dpath

        if isinstance(command, str):
            name = kwargs.get('name', None)
            if name is None:
                name = kwargs['name'] = self.name + '-job-{}'.format(self.num_real_jobs)
            if self.all_depends:
                depends = kwargs.get('depends', None)
                if depends is None:
                    depends = self.all_depends
                else:
                    if not ub.iterable(depends):
                        depends = [depends]
                    depends = self.all_depends + depends
                kwargs['depends'] = depends
            depends = kwargs.pop('depends', None)
            if depends is not None:
                # Resolve any strings to job objects
                if not ub.iterable(depends):
                    depends = [depends]
                try:
                    depends = [
                        self.named_jobs[dep] if isinstance(dep, str) else dep
                        for dep in depends]
                except Exception:
                    print('self.named_jobs = {}'.format(ub.urepr(self.named_jobs, nl=1)))
                    raise
            job = serial_queue.BashJob(command, depends=depends, **kwargs)
        else:
            # Assume job is already a bash job
            job = command
        self.jobs.append(job)

        try:
            if job.name in self.named_jobs:
                raise DuplicateJobError(f'duplicate key {job.name}')
        except Exception:
            raise

        self.named_jobs[job.name] = job

        if not job.bookkeeper:
            self.num_real_jobs += 1
        return job

    @classmethod
    def _backend_classes(cls):
        from cmd_queue import tmux_queue
        from cmd_queue import serial_queue
        from cmd_queue import slurm_queue
        from cmd_queue import airflow_queue
        lut = {
            'serial': serial_queue.SerialQueue,
            'tmux': tmux_queue.TMUXMultiQueue,
            'slurm': slurm_queue.SlurmQueue,
            'airflow': airflow_queue.AirflowQueue,
        }
        return lut

    @classmethod
    def available_backends(cls):
        lut = cls._backend_classes()
        available = [name for name, qcls in lut.items() if qcls.is_available()]
        return available

    @classmethod
    def create(cls, backend='serial', **kwargs):
        """
        Main entry point to create a queue

        Args:
            **kwargs:
                environ (dict | None): environment variables
                name (str): queue name
                dpath (str): queue work directory
                gpus (int): number of gpus
                size (int): only for tmux queue, number of parallel queues
        """
        if backend == 'serial':
            from cmd_queue import serial_queue
            kwargs.pop('size', None)
            self = serial_queue.SerialQueue(**kwargs)
        elif backend == 'tmux':
            from cmd_queue import tmux_queue
            self = tmux_queue.TMUXMultiQueue(**kwargs)
        elif backend == 'slurm':
            from cmd_queue import slurm_queue
            kwargs.pop('size', None)
            self = slurm_queue.SlurmQueue(**kwargs)
        elif backend == 'airflow':
            from cmd_queue import airflow_queue
            kwargs.pop('size', None)
            self = airflow_queue.AirflowQueue(**kwargs)
        else:
            raise UnknownBackendError(backend)
        return self

    def write_network_text(self, reduced=True, rich='auto', vertical_chains=False):
        # TODO: change rich to style
        try:
            import rich as rich_mod
        except ImportError:
            rich_mod = None
        if rich == 'auto':
            rich = rich_mod is not None

        if rich:
            print_ = rich_mod.print
        else:
            print_ = print

        from cmd_queue.util.util_networkx import write_network_text
        import networkx as nx
        graph = self._dependency_graph()
        if reduced:
            print_('\nGraph (reduced):')
            try:
                reduced_graph = nx.transitive_reduction(graph)
                write_network_text(reduced_graph, path=print_, end='',
                                   vertical_chains=vertical_chains)
            except Exception as ex:
                print_(f'ex={ex}')
            print_('\n')
        else:
            print_('\nGraph:')
            write_network_text(graph, path=print_, end='',
                               vertical_chains=vertical_chains)

    def print_commands(self,
                       with_status=False,
                       with_gaurds=False,
                       with_locks=1,
                       exclude_tags=None,
                       style='colors',
                       **kwargs):
        """
        Args:
            with_status (bool):
                tmux / serial only, show bash status boilerplate

            with_gaurds (bool):
                tmux / serial only, show bash guards boilerplate

            with_locks (bool | int):
                tmux, show tmux lock boilerplate

            exclude_tags (List[str] | None):
                if specified exclude jobs submitted with these tags.

            style (str):
                can be 'colors', 'rich', or 'plain'

            **kwargs: extra backend-specific args passed to finalize_text

        CommandLine:
            xdoctest -m cmd_queue.slurm_queue SlurmQueue.print_commands
            xdoctest -m cmd_queue.serial_queue SerialQueue.print_commands
            xdoctest -m cmd_queue.tmux_queue TMUXMultiQueue.print_commands
        """
        colors = kwargs.get('colors', None)
        if colors is not None:
            ub.schedule_deprecation(
                'cmd_queue', 'colors', 'arg',
                migration='use style="plain" | "rich" | "colors" instead',
                deprecate='now')
            if not colors:
                style = 'plain'
        with_rich = kwargs.get('with_rich', None)
        if with_rich is not None:
            ub.schedule_deprecation(
                'cmd_queue', 'with_rich', 'arg',
                migration='use use style="plain" | "rich" | "colors" instead',
                deprecate='now')
            if with_rich:
                style = 'rich'
        if style == 'auto':
            style = 'colors' if colors else 'plain'
            # style = 'rich' if colors else 'plain'

        from cmd_queue.util import util_tags
        exclude_tags = util_tags.Tags.coerce(exclude_tags)
        code = self.finalize_text(
            with_status=with_status,
            with_gaurds=with_gaurds,
            with_locks=with_locks,
            exclude_tags=exclude_tags)
        if style == 'rich':
            from rich.syntax import Syntax
            from rich.panel import Panel
            from rich.console import Console
            console = Console()
            console.print(Panel(Syntax(code, 'bash'), title=str(self.fpath)))
        elif style == 'colors':
            print(ub.highlight_code(f'# --- {str(self.fpath)}', 'bash'))
            print(ub.highlight_code(code, 'bash'))
        elif style == 'plain':
            print(f'# --- {str(self.fpath)}')
            print(code)
        else:
            raise KeyError(f'Unknown style={style}')

    def rprint(self, **kwargs):
        ub.schedule_deprecation(
            'cmd_queue', name='rprint', type='arg',
            migration='print_commands',
        )
        self.print_commands(**kwargs)

    def print_graph(self, reduced=True, vertical_chains=False):
        """
        Renders the dependency graph to an "network text"

        Args:
            reduced (bool): if True only show the implicit dependency forest
        """
        self.write_network_text(reduced=reduced, vertical_chains=vertical_chains)

    def _dependency_graph(self):
        """
        Builds a networkx dependency graph for the current jobs

        Example:
            >>> from cmd_queue import Queue
            >>> self = Queue.create(size=5, name='foo')
            >>> job1a = self.submit('echo hello && sleep 0.5')
            >>> job1b = self.submit('echo hello && sleep 0.5')
            >>> job2a = self.submit('echo hello && sleep 0.5', depends=[job1a])
            >>> job2b = self.submit('echo hello && sleep 0.5', depends=[job1b])
            >>> job3 = self.submit('echo hello && sleep 0.5', depends=[job2a, job2b])
            >>> jobX = self.submit('echo hello && sleep 0.5', depends=[])
            >>> jobY = self.submit('echo hello && sleep 0.5', depends=[jobX])
            >>> jobZ = self.submit('echo hello && sleep 0.5', depends=[jobY])
            >>> graph = self._dependency_graph()
            >>> self.print_graph()
        """
        import networkx as nx
        graph = nx.DiGraph()
        duplicate_names = ub.find_duplicates(self.jobs, key=lambda x: x.name)
        if duplicate_names:
            print('duplicate_names = {}'.format(ub.repr2(duplicate_names, nl=1)))
            raise Exception('Job names must be unique')

        for index, job in enumerate(self.jobs):
            graph.add_node(job.name, job=job, index=index)
        for index, job in enumerate(self.jobs):
            if job.depends:
                for dep in job.depends:
                    if dep is not None:
                        graph.add_edge(dep.name, job.name)
        return graph

    def monitor(self):
        print('monitor not implemented')

    def _coerce_style(self, style='auto', with_rich=None, colors=1):
        # Helper
        if with_rich is not None:
            ub.schedule_deprecation(
                'cmd_queue', 'with_rich', 'arg',
                migration='use style="rich" instead')
            if with_rich:
                style = 'rich'
        if style == 'auto':
            style = 'colors' if colors else 'plain'
        return style
