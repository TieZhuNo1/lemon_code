"""
============================
Project: py09Class
Author:柠檬班-木森
Time:2021/8/31 14:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time
import unittest
from unittestreport import ddt, list_data

@ddt
class TestMusen1(unittest.TestCase):
    data = [
        {'title': "Testmusen1用例1", "data": 11},
        {'title': "Testmusen1用例2", "data": 22},
        {'title': "Testmusen1用例3", "data": 33}]

    @list_data(data)
    def test_musen1_01(self, item):
        time.sleep(0.5)
        print("执行用例:{}".format(item))


@ddt
class TestMusen2(unittest.TestCase):
    data = [
        {'title': "Testmusen2用例1", "data": 11},
        {'title': "Testmusen2用例2", "data": 22},
        {'title': "Testmusen2用例3", "data": 33}]

    @list_data(data)
    def test_musen2_01(self, item):
        time.sleep(0.5)
        print("执行用例:{}".format(item))


