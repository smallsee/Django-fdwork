# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/31 14:17'

from django.conf.urls import url, include

from .views import MovieListView, MovieDetailView


urlpatterns = [
    #课程列表页
    url(r'^list/$', MovieListView.as_view(), name='movie_list'),
    url(r'^detail/$', MovieDetailView.as_view(), name='movie_detail'),

]
