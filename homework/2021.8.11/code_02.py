"""
==========================================
Author:天天
Time:2021/8/11
==========================================
"""


def func_url():
    res = None
    for i in range(6):
        domain = yield res
        res = 'http://' + domain + '/user/login'


if __name__ == '__main__':
    g1 = func_url()
    next(g1)

    print(g1.send("www.1.com"))
    print(g1.send("www.2.com"))
    print(g1.send("www.3.com"))
    print(g1.send("www.4.com"))
    print(g1.send("www.5.com"))
    print(g1.send("www.6.com"))
