"""
==========================================
Author:天天
Time:2021/8/8
==========================================
"""
"""
1、通过列表推导式完成下面数据类型转换

现在有以下数据， li1 = ["{'a':11,'b':2}","[11,22,33,44]"] 

需要转换为以下格式： li1 = [{'a':11,'b':2},[11,22,33,44]] """
li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]

# li1 = [value if index == 0 else eval(value) for index, value in enumerate(li1)]
li1 = [eval(item) for item in li1]
print(li1)
# [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
