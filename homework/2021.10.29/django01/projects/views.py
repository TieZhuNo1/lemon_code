from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    """
    这里会有业务逻辑
    :param request:
    :return:
    """

    return HttpResponse('<h1 style="color:red">接口自动化平台</h1>')
