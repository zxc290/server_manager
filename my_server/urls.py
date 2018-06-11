# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_server_time/', views.get_server_time, name='get_server_time'),
    path('add_server/', views.add_server, name='add_server'),
    path('delete_server/', views.delete_server, name='delete_server'),
    path('edit_server/', views.edit_server, name='edit_server'),
]