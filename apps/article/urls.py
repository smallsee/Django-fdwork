# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/31 14:17'

from django.conf.urls import url, include

from .views import ArticleListView, ArticleDetailView, ArticleAddView


urlpatterns = [
    #课程列表页
    url(r'^list/$', ArticleListView.as_view(), name='article_list'),
    # 本子详情页
    url(r'^detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    # 本子添加页
    url(r'^add/$', ArticleAddView.as_view(), name='article_add'),
]
