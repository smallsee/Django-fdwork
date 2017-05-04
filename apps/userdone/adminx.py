# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/25 15:15'
import xadmin

from .models import UserAsk, UserMessage, UserFavorite, UserComments


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserCommentsAdmin(object):
    list_display = ['user',  'comments', 'add_time']
    search_fields = ['user',  'comments']
    list_filter = ['user', 'comments', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserComments, UserCommentsAdmin)

