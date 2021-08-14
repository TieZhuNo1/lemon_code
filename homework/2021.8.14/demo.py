"""
==========================================
Author:天天
Time:2021/8/14
==========================================
"""
import openpyxl

filename = "data.xlsx"
sheetname = "login"
wb = openpyxl.load_workbook(filename)
sh = wb[sheetname]
rows = list(sh.rows)

res = [dict(zip([c.value for c in rows[0]], [d.value for d in item])) for item in rows[1:]]
print(res)
res.sort(key=lambda x: x['case_id'])
print(res)
res = [exec("item['method']='GET'") or item for item in res]
print(res)
