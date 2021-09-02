"""
==========================================
Author:天天
Time:2021/9/2
==========================================
"""
import unittest
from concurrent.futures.thread import ThreadPoolExecutor

suite = unittest.defaultTestLoader.discover(r'testcase')

suite_list = []
for item in suite:
    for sui_cls in item:
        suite_list.append(sui_cls)


def execute(suite: unittest.TestSuite):
    result = unittest.TestResult()
    res = suite.run(result)
    res = dict(
        fail=len(res.failures),
        error=len(res.errors),
        skip=len(res.skipped),
        all_test=res.testsRun
    )
    return res


with ThreadPoolExecutor(max_workers=4) as pool:
    result = pool.map(execute, suite_list)
    res = {'fail': 0, 'error': 0, 'skip': 0, 'all_test': 0}
    for item in list(result):
        res['fail'] += item['fail']
        res['error'] += item['error']
        res['skip'] += item['skip']
        res['all_test'] += item['all_test']

    print(res)
