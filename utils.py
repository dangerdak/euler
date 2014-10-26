import time


def timed(func):
    def timer(*args):
        t0 = time.time()
        result = func(*args)
        t1 = time.time()
        runtime = t1-t0
        print('Runtime:', runtime)
        return result
    return timer
