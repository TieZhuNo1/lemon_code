from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse
from django.utils import timezone


# Create your views here.


def index(request):
    """
    首页面视图
    """

    # return HttpResponse("接口自动化平台")
    now = timezone.now()
    return render(request, 'projects/index.html',context={
        'now':now
    })


def detail(request, pid):
    """
    项目详情视图
    """
    print(type(pid))
    return HttpResponse("项目id为{}的详情页".format(pid))


def project_list(request, year, month):
    """
    项目列表视图
    """
    html = ''' 返回了{}年{}月的项目列表<br/>
    <a href="{}">前程贷</a><br/>
    <a href="{}">微信小程序</a><br/>
    <a href="{}">微信公众号</a>
    '''

    return HttpResponse(html.format(year, month,
                                    reverse('projects:detail', args=(1,)),
                                    reverse('projects:detail', args=(2,)),
                                    reverse('projects:detail', args=(3,))
                                    ))
