from python.workers.worker import Worker


class WorkerService:

    def run(self, func, *args):

        Worker.start(
            func,
            *args
        )