"""
==========================================
Author:天天
Time:2021/8/8
==========================================
"""
# 3、通过字典推导式，颠倒字典的键名和值:将{'py': "python09", 'java': "java09"} 转换为： {'python09': "py", 'java09': "java"}
dic_1 = {'py': "python09", 'java': "java09"}
dic_2 = {value: key for key, value in dic_1.items()}
print(dic_2)
# {'python09': 'py', 'java09': 'java'}
