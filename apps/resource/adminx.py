# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/25 15:15'
import xadmin

from .models import Resource


class ResourceAdmin(object):
    list_display = ['name', 'user', 'resource_url', 'fav_nums', 'image', 'click_nums', 'tag', 'add_time']
    search_fields = ['name', 'user', 'resource_url', 'fav_nums', 'image', 'click_nums', 'tag']
    list_filter = ['name', 'user', 'resource_url', 'fav_nums', 'image', 'click_nums', 'add_time', 'tag']
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Resource, ResourceAdmin)
