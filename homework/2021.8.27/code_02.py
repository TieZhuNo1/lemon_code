"""
==========================================
Author:天天
Time:2021/8/27
==========================================
"""
from threading import Thread
import time

url_list = [f'url_{i + 1}' for i in range(100)]
it = iter(url_list)


class MyThread(Thread):
    def run(self):
        while True:
            try:
                print("{}请求{}".format(self, next(it)))
                time.sleep(0.5)
            except StopIteration:
                print("所有地址请求完毕,关闭{}".format(self))
                break


if __name__ == '__main__':
    s_t = time.time()
    # for i in range(4):
    #     t = MyThread(name='线程{}'.format(i + 1))
    #     t.start()
    t1 = MyThread(name='线程1')
    t2 = MyThread(name='线程2')
    t3 = MyThread(name='线程3')
    t4 = MyThread(name='线程4')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    e_t = time.time()
    print("执行时间:{}".format(e_t - s_t))
