import time


def time_test(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        print(f'func time is: {et - st}')
        return res

    return wrapper

