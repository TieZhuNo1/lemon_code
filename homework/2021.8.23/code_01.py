"""
==========================================
Author:天天
Time:2021/8/23
==========================================
"""
import time


class MyType(type):

    def __new__(cls, name, bases, attrs, *args, **kwargs):
        my_cls = super().__new__(cls, name, bases, attrs)
        setattr(my_cls, 'class_name', name)
        setattr(my_cls, 'create_time', time.time())
        return my_cls


if __name__ == '__main__':
    mycls = MyType('TianTian', (), {})
    print(getattr(mycls, 'class_name'))
    print(getattr(mycls, 'create_time'))
