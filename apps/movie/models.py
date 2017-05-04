# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models
from users.models import UserProfile
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    user = models.ForeignKey(UserProfile, verbose_name=u'发布者', default='')
    detail = UEditorField(verbose_name=u'课程详情', width=600, height=300, imagePath="movie/ueditor/",
                          filePath="movie/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')
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


class Lesson(models.Model):
    movie = models.ForeignKey(Movie, verbose_name=u'视频')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Movie, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    url = models.CharField(max_length=200, default='', verbose_name=u'视频地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name