"""
==========================================
Author:天天
Time:2021/8/11
==========================================
"""

li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]

generator_1 = (item % 2 for item in li if item > 5)


if __name__ == '__main__':
    for each in generator_1:
        print(each)