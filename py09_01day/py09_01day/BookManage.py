"""
============================
Project: py09Class
Author:柠檬班-木森
Time:2021/8/5 20:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pymysql


class DB:
    """项目涉及到数据库的增删查改，咱们封装数据库对应的操作方法来处理
    查询的方法
    增删改的方法
    """

    def __init__(self):
        # self.con = pymysql.connect(
        #     user='root',
        #     password='mysql',
        #     host="localhost",
        #     port=3306,
        #     database='test'
        # )
        self.con = pymysql.connect(
            user='root',
            password='123456',
            host="192.168.66.172",
            port=3306,
            database='library'
        )
        self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)

    def query_sql(self, sql):
        """
        查询sql的方法
        :param sql: sql语句
        :return: 查询到的结果
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update_sql(self, sql):
        """
        :param sql: sql语句
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        """关闭游标，断开连接"""
        self.cur.close()
        self.con.close()


class Books(DB):

    def add_book(self):
        """添加图书"""
        print("**********添加图书*****************")
        name = input("请输入书名:")
        position = input("请输入图书存放的位置:")
        if name and position:
            sql = f'insert into books(name,position) value("{name}","{position}")'
            self.update_sql(sql)
            print('添加成功！')
        else:
            print("添加失败，书名和位置均不能为空！")
        n = input("继续添加请输入1，回车返回主菜单:")
        # 判断用户输入的是否为1，为1则再次调用添加图书的方法
        if n == '1':
            self.add_book()

    def update_book(self):
        """修改图书"""
        print("**********修改图书*****************")
        id = input("请输入要修改的图书id")
        # 查询输入的id对应的书籍是否存在
        res = self.query_sql(f'select * from books where id={id}')
        if res:
            # 打印图书的信息
            print('当前图书的信息:', res)
            # 进行修改
            name = input("请输入新的书名,不修改输入回车：") or res[0]['name']
            position = input("请输入图书存放的位置,不修改输入回车：") or res[0]['position']
            sql = f'update books set name="{name}",position="{position}" where id={id}'
            self.update_sql(sql)
            print('修改成功!')
        else:
            print("您输入的书籍id不存在")

        n = input("继续修改请输入1，回车返回主菜单:")
        if n == '1':
            self.update_book()

    def del_book(self):
        """删除图书"""
        print("**********删除图书*****************")
        id = input("请输入删除图书的id:")
        # 查询输入的id对应的书籍是否存在
        res = self.query_sql(f'select * from books where id={id}')
        if res:
            print("您要删除的书籍信息如下：", res)
            is_delete = input("确认删除请输入1，取消删除敲回车")
            if is_delete == '1':
                sql = f'delete from books where id={id}'
                self.update_sql(sql)
                print("删除成功")
        else:
            print("您输入的书籍id不存在")
        # 判断是否要继续删除
        n = input("继续删除请输入1，回车返回主菜单:")
        if n == '1':
            self.del_book()

    def query_book(self):
        """查询图书"""
        print("**********查询图书*****************")
        name = input("请输入要查询的图书名:")
        sql = f'select * from books where name="{name}"'
        res = self.query_sql(sql)
        if res:
            for i in res:
                print(i)
        else:
            print("图书馆中暂无该书籍！")
        n = input("继续查询请输入1，回车返回主菜单:")
        if n == '1':
            self.query_book()

    def book_list(self):
        """图书列表"""
        sql = 'select * from books'
        res = self.query_sql(sql)
        print("**********图书列表*****************")
        for i in res:
            print(f"编号：{i['id']},书名:{i['name']},位置:{i['position']}，状态：{i['status']},借阅人：{i['borrorwer']}")
            # print("编号：{},书名:{},位置:{}，状态：{},借阅人：{}".format(i['id'], i['name'], i['position'], i['status'],
            #                                               {i['borrorwer']}))
        print("返回主菜单页面")

    def revert_book(self):
        """归还图书"""

    def lend_book(self):
        """出借图书"""
        print("**********借阅图书*****************")
        id = input("请输入要借阅的图书id")
        # 查询输入的id对应的书籍是否存在
        res = self.query_sql(f'select * from books where id={id}')
        if res:
            # 打印图书的信息
            print('当前图书的信息:', res)
            # 进行修改
            name = input("请输入新的书名,不修改输入回车：") or res[0]['name']
            position = input("请输入图书存放的位置,不修改输入回车：") or res[0]['position']
            sql = f'update books set name="{name}",position="{position}" where id={id}'
            self.update_sql(sql)
            print('修改成功!')
        else:
            print("您输入的书籍id不存在")

        n = input("继续添加请输入1，回车返回主菜单:")
        if n == '1':
            self.update_book()
    def quit(self):
        """退出"""
        self.close()
        print("程序退出！！！")

    def print_menu(self):
        """打印菜单"""
        print('-----------菜单------------')
        print("【1】:添加图书")
        print("【2】:修改图书")
        print("【3】:删除图书")
        print("【4】:查询图书")
        print("【5】:图书列表")
        print("【6】:出借图书")
        print("【7】:归还图书")
        print("【8】:退出")

    def main(self):
        print("---------------欢迎进入柠檬图书管理系统---------------")
        while True:
            self.print_menu()
            number = input("请输入你的选项:")
            if number == '1':
                self.add_book()
            elif number == '2':
                self.update_book()
            elif number == '3':
                self.del_book()
            elif number == '4':
                self.query_book()
            elif number == '5':
                self.book_list()
            elif number == '6':
                self.lend_book()
            elif number == '7':
                self.revert_book()
            elif number == '8':
                self.quit()
                break
            else:
                print("您输入的选项有误！")


if __name__ == '__main__':
    book = Books()
    book.main()
