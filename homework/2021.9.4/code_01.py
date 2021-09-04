"""
==========================================
Author:天天
Time:2021/9/4
==========================================
"""
import socket
from concurrent.futures.thread import ThreadPoolExecutor
import re


class TCPServer:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 第二步：绑定ip和端口:bind
        self.sock.bind(('127.0.0.1', 7799))
        print("TCP服务绑定的地址：127.0.0.1:7799")
        # 第三步：开启监听
        self.sock.listen(100)

    def handle_request(self, cil_sock, addr):
        """处理客户端请求的方法"""
        print("客户端{}建立了链接".format(addr))
        # 第五步：接收客户端传递的数据(接收到的是二进制的数据)
        content = b''
        while True:
            res = cil_sock.recv(1024)
            content += res
            # 判断接收到的数据是否少于1024个字节，如果少于说明数据接收完了
            if len(res) < 1024:
                break

        request_conetnt = content.decode()
        print("客户端发送过来的数据为:", )
        # 调用解析数据的方法对请求的http数据包进行解析
        html=self.parser_request(request_conetnt) or 'blank.html'

        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: text/html;charset=utf-8\r\n'
        header += '\r\n\r\n'
        # 读取网页内容
        with open(html, 'rb') as f:
            body = f.read()
        # 拼接响应头和响应体
        data = header.encode() + body
        # 第六步：给客户端返回数据
        cil_sock.send(data)
        # 关闭处理客户端会话的套接字
        cil_sock.close()

    def parser_request(self, content):
        """解析客户端的请求信息"""
        # 1、获取请求方法是什么
        request_line = content.split('\r\n')[0]
        method = re.search(r'(.*?) ', request_line).group(1)
        # 2、获取请求的路径
        path = re.search(r' (.*?) ', request_line).group(1)
        # 3、获取请求头
        header = content.split('\r\n\r\n')[0].split('\r\n')[1:]
        headers = {item.split(':')[0]: item.split(':')[1] for item in header}
        # 4、获取请求参数
        # 获取请求体
        body = content.split('\r\n\r\n')[1]
        # 判断是否是否有查询字符串参数
        if '?' in path:
            params = path.split('?')[1]
            path = path.split('?')[0]
            pass

        # 判断是否有json参数

        # 判断是否有表单参数
        if path == '/account/login':
            html = 'login.html'
            return html
        elif path=='/account/register':
            html = 'register.html'
            return html


    def run(self):
        # 创建一个线程池，设置20个线程
        with ThreadPoolExecutor(max_workers=20) as pool:
            while True:
                # 第四步：等待客户端发起请求，建立连接
                cil_sock, addr = self.sock.accept()
                # 当客户端建立连接之后，往线程池中提交一个处理的任务
                # pool.submit(self.handle_request, cil_sock, addr)
                self.handle_request(cil_sock, addr)


if __name__ == '__main__':
    TCPServer().run()
