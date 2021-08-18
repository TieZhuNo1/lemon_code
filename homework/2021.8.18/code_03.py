"""
==========================================
Author:天天
Time:2021/8/18
==========================================
"""


class MyDecorator:
    def __init__(self, obj):
        self._obj = obj

    def __call__(self, *args, **kwargs):
        print("类装饰{}".format(self._obj))
        return self._obj(*args, **kwargs)


if __name__ == '__main__':
    @MyDecorator
    class Demo:
        def __init__(self, x):
            self.x = x
            print(f"Demo类初始化,输出x:{x}")


    @MyDecorator
    def demo(y):
        print(f"demo函数输出y:{y}")


    Demo(1)
    demo(2)
