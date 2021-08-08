"""
==========================================
Author:天天
Time:2021/8/8
==========================================
"""
"""
2、 Names=['python','java','php','c','c++','django','unittest','pytest','pymysql'],请通过列表推导式，获取names中字符串长度大于4的元素
"""

Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest', 'pymysql']
Names_4 = [item for item in Names if len(item) > 4]
print(Names_4)
# ['python', 'django', 'unittest', 'pytest', 'pymysql']
