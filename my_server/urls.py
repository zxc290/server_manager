# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_server_time/', views.get_server_time, name='get_server_time'),
    path('set_server_time/', views.set_server_time, name='set_server_time')
]