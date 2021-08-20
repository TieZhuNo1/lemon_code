"""
==========================================
Author:天天
Time:2021/8/20
==========================================
"""


class Demo(object):
    __slots__ = ('title', 'money', 'data')

    def __init__(self, title, money, data):
        self.title = title
        self.money = money
        self.data = data

    def __setattr__(self, key, value):
        if key == 'title':
            if isinstance(value, str):
                super().__setattr__(key, value)
            else:
                raise TypeError('title属性只能设置为字符串')
        elif key == 'money':
            if isinstance(value, int):
                super().__setattr__(key, value)
            else:
                raise TypeError('money属性只能设置为int')
        else:
            super().__setattr__(key, value)

    def __delattr__(self, name):
        if name == 'data':
            raise Exception('data属性不能被删除')
        else:
            super().__delattr__(name)

    def __getattribute__(self, name):
        if name == 'money':
            if super().__getattribute__(name) < 0:
                return 0
            else:
                return super().__getattribute__(name)
        else:
            return super().__getattribute__(name)
