import threading


class Worker:

    @staticmethod
    def start(target, *args):

        thread = threading.Thread(
            target=target,
            args=args,
            daemon=True
        )

        thread.start()

        return thread