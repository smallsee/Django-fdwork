# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/31 14:17'

from django.conf.urls import url, include

from .views import BookListView, BookDetailView, BookAddView
from .upload import upload_image

urlpatterns = [
    #本子列表页
    url(r'^list/$', BookListView.as_view(), name='book_list'),
    #本子详情页
    url(r'^detail/(?P<book_id>\d+)/$', BookDetailView.as_view(), name='book_detail'),
    #本子添加页
    url(r'^add/$', BookAddView.as_view(), name='book_add'),
    #本子编辑器图片上传
    url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]
