# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/25 15:15'
import xadmin

from .models import Article


class Articledmin(object):
    list_display = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'tag', 'add_time']
    search_fields = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'tag']
    list_filter = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'tag', 'add_time']
    style_fields = {"detail": "ueditor"}

xadmin.site.register(Article, Articledmin)
