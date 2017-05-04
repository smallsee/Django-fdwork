# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/25 15:15'
import xadmin


from .models import Movies, Video


class MovieAdmin(object):
    list_display = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'user', 'desc', 'fav_nums', 'image', 'click_nums', 'add_time']


class VideoAdmin(object):
    list_display = ['video_name', 'movie', 'add_time']
    search_fields = ['video_name', 'movie']
    list_filter = ['video_name', 'movie', 'add_time']

xadmin.site.register(Movies, MovieAdmin)
xadmin.site.register(Video, VideoAdmin)

