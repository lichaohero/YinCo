#-*-coding:utf-8-*-
from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^v1/users', views.users),
]