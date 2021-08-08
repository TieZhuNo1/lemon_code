"""
============================
Project: py09Class
Author:柠檬班-木森
Time:2021/8/5 20:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pymysql

# pymysql连接数据库
con = pymysql.connect(
    user='root',
    password='mysql',
    host="localhost",
    port=3306,
    # database='test'
)
# 创建一个游标对象
cur = con.cursor(cursor=pymysql.cursors.DictCursor)

# # 执行查询语句sql
# sql = ' select * from test.books'
# res = cur.execute(sql)
# print(res)
#
# # 获取查询的结果
# result = cur.fetchall()
# print(result)


# 执行增删改的sql
sql = 'insert into test.books(name,position) value("天龙八部2","a区1号架1层")'
res = cur.execute(sql)

# 提交事务
# con.commit()
print(res)