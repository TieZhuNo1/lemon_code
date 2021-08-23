"""
==========================================
Author:天天
Time:2021/8/23
==========================================
"""
from functools import wraps

from scripts.handle_request import HandleRequest

"""
什么时候需要用到元类？
    1、动态创建类，在创建类的过程中要自定义类属性和方法


需求：自定义元类来实现动态创建测试类和测试方法

"""
import unittest


def update_test_func(func, value):
    @wraps(func)
    def wrapper(self, **kwargs):
        return func(self, value)

    return wrapper


class MyMateClass(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        # 通过元类创建一个类
        test_cls = super().__new__(cls, name, bases, attrs)
        # 遍历属性Cases
        for index, value in enumerate(attrs['Cases']):
            # func =test_cls.test_perform
            func = getattr(test_cls, 'perform')
            test_func = update_test_func(func, value)
            # 动态给test_cls这个类 添加方法
            setattr(test_cls, 'test_{}'.format(index), test_func)
        return test_cls


class BaseApiCase:
    """用例执行的基本类"""

    def perform(self, case):
        """用例执行的方法"""
        print("测试数据：", case)

        # 1、用例数据的处理

        # 2、接口请求
        do_request = HandleRequest()
        res = do_request.send(url=case['url'],  # url地址
                                   # method=case.method,    # 请求方法
                                   data=case['data'],  # 请求参数
                                   # is_json=True   # 是否以json格式来传递数据, 默认为True
                                   )
        # 3、响应数据提取
        actual_value = res.json()
        # 4、断言
        assert (case['expected'] == actual_value)


if __name__ == '__main__':
    import unittestreport
    import json

    # 通过自定义的元类创建类
    #
    #
    with open('test_login.json', 'r', encoding='utf-8') as f:
        cases = {'Cases': json.load(f)}
    Musen = MyMateClass('Musen', (unittest.TestCase, BaseApiCase), cases)

    # # 加载测试类的用例到测试套件
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Musen)
    # 运行用例
    unittestreport.TestRunner(suite, templates=2).run()
