"""
==========================================
Author:天天
Time:2021/8/16
==========================================
"""


class LoginRequire:
    __login = False
    c_username = "lemonban"
    c_password = "123456"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if LoginRequire.__login:
            return self.func(*args, **kwargs)
        elif self.login():
            return self.func(*args, **kwargs)
        else:
            print("账号或密码错误，登录失败，执行权限不足")

    def login(self):
        username = input("请输入账号:")
        password = input("请输入密码:")
        if username == LoginRequire.c_username and password == LoginRequire.c_password:
            LoginRequire.__login = True
            return True
        else:
            return False


@LoginRequire
def work_01(a, b):
    print(f"输出{a}+{b}={a + b}")


@LoginRequire
def work_02(a, b):
    print(f"输出{a}*{b}={a * b}")


if __name__ == '__main__':
    work_01(1, 2)
    work_02(5, 6)
