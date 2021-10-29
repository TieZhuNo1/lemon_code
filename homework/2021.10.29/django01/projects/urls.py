"""
==========================================
Author:天天
Time:2021/10/29
==========================================
"""
from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index)
]
