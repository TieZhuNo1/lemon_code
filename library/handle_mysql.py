# -*- coding: utf-8 -*-
import random

import pymysql


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host="192.168.66.172",  # mysql服务器ip或者域名
                                    user="root",  # 用户名
                                    password="123456",
                                    db="library",  # 要连接的数据库名
                                    port=3306,  # 数据库端口号, 默认为3306
                                    # charset='utf8',  # 数据库编码为utf8, 不能设为utf-8
                                    charset='utf8mb4',  # 数据库编码为utf8, 不能设为utf-8
                                    # 默认返回的结果为元祖或者嵌套元祖的列表
                                    # 可以指定cursorclass为DictCursor, 那么返回的结果为字典或者嵌套字典的列表
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.cursor = self.conn.cursor()

    def search(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def add(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except:
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_book_mysql(self, book_name, book_position):
        sql = f"insert into books(name,position) value('{book_name}','{book_position}');"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def del_book_mysql(self, book_id):
        sql = f"delete from books where id = '{book_id}';"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def update_book_mysql(self, book_id, book_name, book_position):
        sql = f"UPDATE books SET name = '{book_name}', position = '{book_position}' WHERE id = '{book_id}'"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def search_book_mysql_by_name(self, book_name, is_more=False):
        sql = f"select * from books where name = '{book_name}'"
        self.cursor.execute(sql)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def search_book_mysql_by_id(self, book_id, is_more=False):
        sql = f"select * from books where id = '{book_id}'"
        self.cursor.execute(sql)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def search_book_mysql_all(self, book_id, is_more=False):
        sql = f"select * from books where id = '{book_id}'"
        self.cursor.execute(sql)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

if __name__ == '__main__':
    # 当封装好了一个类之后, 要在下面自测一下
    do_mysql = HandleMysql()
    # do_mysql.add_book("python入门到精通", "A区2号架3层")
    # do_mysql.update_book(4, '测试1', '测试2')
    # do_mysql.del_book(4)
    res=do_mysql.search_book_mysql("python入门到精")
    print(res)
    pass
