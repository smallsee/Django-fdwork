# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/25 15:15'
import xadmin

from .models import Book


class BookAdmin(object):
    list_display = ['name', 'user', 'fav_nums', 'image', 'click_nums', 'tag', 'add_time']
    search_fields = ['name', 'user', 'fav_nums', 'image', 'click_nums', 'tag']
    list_filter = ['name', 'user', 'fav_nums', 'image', 'click_nums', 'add_time', 'tag']
    style_fields = {"book_list": "ueditor"}


xadmin.site.register(Book, BookAdmin)
