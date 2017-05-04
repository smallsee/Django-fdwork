# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/31 14:17'

from django.conf.urls import url, include

from .views import UserCenterListView, AddCommitsView, UserCenterMovieView, \
                    UserCenterArticleView, UserCenterBookView, AddFavView, UserCenterCollectView, UserCenterMusiceView, \
                    UserCenterResourceView


urlpatterns = [
    #用户中心页
    url(r'^info/(?P<user_id>\d+)/$', UserCenterListView.as_view(), name='user_info'),
    #用户中心视频页
    url(r'^info/movie/(?P<user_id>\d+)/$', UserCenterMovieView.as_view(), name='user_movie'),

    #用户中心文章页
    url(r'^info/article/(?P<user_id>\d+)/$', UserCenterArticleView.as_view(), name='user_article'),

    #用户中心本子页
    url(r'^info/book/(?P<user_id>\d+)/$', UserCenterBookView.as_view(), name='user_book'),
    #用户中心音乐页
    url(r'^info/music/(?P<user_id>\d+)/$', UserCenterMusiceView.as_view(), name='user_music'),
    #用户中心资源页
    url(r'^info/resource/(?P<user_id>\d+)/$', UserCenterResourceView.as_view(), name='user_resource'),
    #用户中心收藏页
    url(r'^info/collect/(?P<user_id>\d+)/$', UserCenterCollectView.as_view(), name='user_collect'),

    #添加评论也
    url(r'^add_commit/$', AddCommitsView.as_view(), name='add_commit'),
    #添加收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),


    #图片上传
    url(r'^upload_image/$', UserCenterListView.as_view(), name='upload_image'),
]
