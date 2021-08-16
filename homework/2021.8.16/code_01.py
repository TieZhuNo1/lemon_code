"""
==========================================
Author:天天
Time:2021/8/16
==========================================
"""


def check_b(func):
    def wrapper(a, b):
        if b == 0:
            print("参数b不能为零")
        else:
            return func(a, b)

    return wrapper


@check_b
def work(a, b):
    res = a / b
    print('a除B的结果为:', res)


if __name__ == '__main__':
    work(4, 2)
    work(3, 0)
