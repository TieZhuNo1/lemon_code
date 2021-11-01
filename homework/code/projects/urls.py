"""
==========================================
Author:天天
Time:2021/11/1
==========================================
"""
from django.urls import path, include, re_path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<path:pid>/', views.detail, name='detail'),
    re_path(r'^list/(?P<year>\d{4})/(?P<month>[1-9]|1[0-2])/$', views.project_list, name='list')
]
