# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/31 14:17'

from django.conf.urls import url, include
from .views import MusicListView, MusicDetailView, MusicAddView


urlpatterns = [
    #音乐列表页
    url(r'^list/$', MusicListView.as_view(), name='music_list'),
    # 音乐详情页
    url(r'^detail/(?P<music_id>\d+)/$', MusicDetailView.as_view(), name='music_detail'),
    # 音乐添加液
    url(r'^add/$', MusicAddView.as_view(), name='music_add'),
]
