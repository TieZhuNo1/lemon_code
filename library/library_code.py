"""
==========================================
Author:不二
Time:2021/8/4
==========================================
"""
from handle_mysql import HandleMysql


class Library:
    def __init__(self):
        self.do_mysql = HandleMysql()

    def library_menu(self):
        print("-------------欢迎进入图书管理系统-------------")
        print("-------------菜单-------------")
        print("""【1】：添加图书
【2】：修改图书
【3】：删除图书
【4】：查询图书
【5】：图书列表
【6】：出借图书
【7】：归还图书
【8】：退出""")
        option = input("请输入选项：")
        print(option)

    def add_book(self):
        while True:
            print("***************添加图书***************")
            book_name = input("请输入书名：")
            book_position = input("请输入图书位置：")
            if not (book_name and book_position):
                print("书名和位置不可为空")
                continue
            else:
                self.do_mysql.add_book_mysql(book_name, book_position)
                print("图书添加成功")
            option = input("继续添加请输入1，回车退回主菜单")
            while not (option == "1" or option == ""):
                print("请输入正确指令")
                option = input("继续添加请输入1，回车退回主菜单")
            if option == "1":
                continue
            elif option == "":
                break

    def update_book(self):
        while True:
            print("***************修改图书***************")
            book_id = input("输入修改的图书id：")
            if not book_id:
                print("图书id不可为空")
                continue
            try:
                int(book_id)
            except:
                print("图书id需为正整数")
                continue
            else:
                if int(book_id) <= 0:
                    print("图书id需为正整数")
                    continue
                res = self.do_mysql.search_book_mysql_by_id(book_id)
                if not res:
                    print("未查询到图书id {}".format(book_id))
                    continue
                else:
                    print("当前数据为：{}".format(res))
                book_name = input("重新输入书名，不修改输入回车：")
                if book_name == "":
                    break
                else:
                    book_position = input("请输入图书位置：")
                    if book_position == "":
                        break
                    else:
                        self.do_mysql.update_book_mysql(book_id, book_name, book_position)
                        print("*****修改成功*****")
            option = input("继续修改请输入1，回车退回主菜单")
            while not (option == "1" or option == ""):
                print("请输入正确指令")
                option = input("继续修改请输入1，回车退回主菜单")
            if option == "1":
                continue
            elif option == "":
                break
    def show_all_book(self):
        pass

if __name__ == '__main__':
    dd = Library()
    # dd.library_menu()
    # dd.add_book()
    dd.update_book()
