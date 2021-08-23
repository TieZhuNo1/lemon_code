"""
==========================================
Author:天天
Time:2021/8/23
==========================================
"""


def func(n):
    if n == 1:
        return 100
    elif n == 2:
        return 100 + 100 / 2 * 2
    else:
        return func(n - 1) + (func(n - 1) - func(n - 2)) / 2


if __name__ == '__main__':
    print(func(10))
