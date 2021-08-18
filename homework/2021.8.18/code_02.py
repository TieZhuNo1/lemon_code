"""
==========================================
Author:天天
Time:2021/8/18
==========================================
"""
import random


class Demo(object):
    _instance_list = []

    def __new__(cls, *args, **kwargs):
        if len(cls._instance_list) < 5:
            new_instance = object.__new__(cls, *args, **kwargs)
            cls._instance_list.append(new_instance)
            return new_instance
        else:
            return random.choice(cls._instance_list)


if __name__ == '__main__':
    a1 = Demo()
    a2 = Demo()
    a3 = Demo()
    a4 = Demo()
    a5 = Demo()
    a6 = Demo()
    a7 = Demo()
    print(id(a1), id(a2), id(a3), id(a4), id(a5), id(a6), id(a7))
