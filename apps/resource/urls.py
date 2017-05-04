# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/31 14:17'

from django.conf.urls import url, include
from .views import ResourceListView, ResourceDetailView, ResourceAddView



urlpatterns = [
    #资源列表页
    url(r'^list/$', ResourceListView.as_view(), name='resource_list'),
    # 资源详情页
    url(r'^detail/(?P<resource_id>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    #资源添加页
    url(r'^add/$', ResourceAddView.as_view(), name='resource_add'),
]
