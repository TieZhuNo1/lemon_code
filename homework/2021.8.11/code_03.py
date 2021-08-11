"""
==========================================
Author:天天
Time:2021/8/11
==========================================
"""


def func(array, x):
    list_1 = [item for item in set(array) if item > x]
    count = len(list_1)
    li = [item for item in array if item < x and item % 2 == 0]
    return count, li


if __name__ == '__main__':
    array = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22, 10, 11, 22]
    x = 20
    count, li = func(array, x)
    print(count, li)
