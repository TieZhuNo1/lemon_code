"""
==========================================
Author:天天
Time:2021/8/20
==========================================
"""


class MyList:
    def __init__(self, li):
        self.li = li

    def __sub__(self, other):
        return [item for item in self.li if item not in other.li]


if __name__ == '__main__':
    li1 = MyList([11, 22, 33, 22, 44])
    li2 = MyList([1, 22])
    res = li1 - li2
    print(res)
