"""
==========================================
Author:天天
Time:2021/11/1
==========================================
"""
from django.urls import path

from . import views

app_name = 'testcases'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:tid>/', views.detail, name='detail'),
    path('list/<int:year>/<int:month>/', views.testcase_list, name='list')
]
