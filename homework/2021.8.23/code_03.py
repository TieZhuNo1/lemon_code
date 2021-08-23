"""
==========================================
Author:天天
Time:2021/8/23
==========================================
"""
p_list = [f"编号{item + 1}" for item in range(40)]

# print(p_list)

index = 0
for i in range(20):
    if len(p_list) - index >= 9:
        index = index + 9 - 1
        print(p_list.pop(index))
    else:
        index = index + 9 - 1 - len(p_list)
        print(p_list.pop(index))
