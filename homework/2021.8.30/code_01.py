"""
==========================================
Author:天天
Time:2021/8/30
==========================================
"""
from multiprocessing import Process, Queue
import time


def create_data(name, datas):
    while True:
        if datas.qsize() < 50:
            for i in range(200):
                datas.put("{}生成数据{}".format(name, time.time()))
            time.sleep(1)


def get_data(name, datas):
    while True:
        if datas.qsize() > 10:
            for i in range(20):
                data = datas.get()
                print("{}获取到数据:{}".format(name, data))
        else:
            time.sleep(2)


def main():
    datas = Queue()
    c = Process(target=create_data, args=('生产函数', datas))
    c.start()
    for i in range(5):
        g = Process(target=get_data, args=(f'获取函数—{i + 1}', datas))
        g.start()


if __name__ == '__main__':
    main()
