# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/25 15:15'
import xadmin

from .models import Music, Lesson, LessonMusic


class MusicAdmin(object):
    list_display = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'tag', 'add_time']
    search_fields = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'tag']
    list_filter = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'tag', 'add_time']
    style_fields = {"detail": "ueditor"}


class LessonAdmin(object):
    list_display = ['music', 'name', 'add_time']
    search_fields = ['music', 'name']
    list_filter = ['music__name', 'name', 'add_time']


class LessonMusicAdmin(object):
    list_display = ['lesson', 'name', 'singer',  'name', 'add_time']
    search_fields = ['lesson', 'name', 'singer', 'image', 'name']
    list_filter = ['lesson', 'name', 'singer', 'image', 'name', 'add_time']


xadmin.site.register(Music, MusicAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(LessonMusic, LessonMusicAdmin)
