import threading


# Adapted from https://gist.github.com/Depado/7925679
def periodic_task(interval):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            stop = threading.Event()

            def inner_wrap():
                while not stop.is_set():
                    stop.wait(interval)
                    try:
                        function(*args, **kwargs)
                    except Exception:
                        logger.exception('Periodic task failed')

            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap
