from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse


# Create your views here.


def index(request):
    return HttpResponse('测试用例的首页')


def detail(request, tid):
    return HttpResponse('id为{}的用例的详情页'.format(tid))


def testcase_list(request, year, month):
    html = '''返回了{}年{}月的用例列表<br/>
    <a href="{}">注册成功不带用户名</a></br>
    <a href="{}">注册成功管理员</a></br>
    <a href="{}">注册成功普通用户</a>            
    '''

    return HttpResponse(html.format(year, month,
                                    reverse('testcases:detail', args=(1,)),
                                    reverse('testcases:detail', args=(2,)),
                                    reverse('testcases:detail', args=(3,))
                                    ))
