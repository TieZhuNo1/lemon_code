"""
==========================================
Author:天天
Time:2021/8/16
==========================================
"""


def re_run(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                try:
                    func(*args, **kwargs)
                except AssertionError:
                    continue
                else:
                    break

        return wrapper

    return decorator


@re_run(3)
def work_ok():
    print("正常运行")


@re_run(3)
def work_error_01():
    print("运行失败-AssertionError")
    raise AssertionError


@re_run(3)
def work_error_02():
    print("运行失败-KeyError")
    raise KeyError


if __name__ == '__main__':
    work_ok()
    work_error_01()
    work_error_02()
