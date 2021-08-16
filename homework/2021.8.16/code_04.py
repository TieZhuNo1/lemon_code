"""
==========================================
Author:天天
Time:2021/8/16
==========================================
"""
import time


def run_time(second: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            if end - start > second:
                print("{}运行时间：{}".format(func.__name__, end - start))

        return wrapper

    return decorator


@run_time(1)
def work():
    time.sleep(2)


if __name__ == '__main__':
    work()
