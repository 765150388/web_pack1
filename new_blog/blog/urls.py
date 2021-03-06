#coding:utf-8
__author__ = 'zzj'
__date__ = '2017/11/19 14:05'

from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^login', do_login, name='login'),
    url(r'^category/$', category, name='category'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^$', index, name='index'),
    url(r'^article/$', article, name='article')
]
