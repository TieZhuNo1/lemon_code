"""
==========================================
Author:天天
Time:2021/8/18
==========================================
"""


def singleton(cls):
    _instance = {}

    def decorator(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]

    return decorator


if __name__ == '__main__':
    @singleton
    class Demo:
        def __init__(self):
            print("实例化")


    a = Demo()
    b = Demo()
    print(id(a), id(b))
