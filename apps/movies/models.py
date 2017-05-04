# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models
from users.models import UserProfile
# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'视频名')
    desc = models.CharField(max_length=300, verbose_name=u'视频描述')
    user = models.ForeignKey(UserProfile, verbose_name=u'发布者', default='')
    detail = UEditorField(verbose_name=u'视频详情', width=600, height=300, imagePath="movie/ueditor/",
                          filePath="movie/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')
    category = models.CharField(verbose_name=u'视频类型', max_length=50, choices=(('dh', u'动画'), ('fj', u'番剧'), ('gc', u'鬼畜'), ('kj', u'科技'), ('dsj', u'电视剧'), ('lf', u'里番')), default='dh')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='movie/%Y/%m', verbose_name=u'封面图', max_length=300)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(default='', max_length=10, verbose_name=u'视频标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频作品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    movie = models.ForeignKey(Movies, verbose_name=u'视频')
    video_name = models.CharField(max_length=100, verbose_name=u'章节名')
    url = models.CharField(max_length=200, default='', verbose_name=u'视频地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.video_name


