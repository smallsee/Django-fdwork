# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

from users.models import UserProfile
# Create your models here.


class Music(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'专辑名')
    tag = models.CharField(verbose_name=u'音乐类型', max_length=50, choices=(('zy', u'治愈'), ('rx', u'燃向'), ('love', u'恋爱'), ('sad', u'悲伤'), ('cyy', u'纯音乐'), ('code', u'代码')), default='grzh')
    user = models.ForeignKey(UserProfile, verbose_name=u'发布者', default='')
    desc = models.CharField(max_length=300, verbose_name=u'音乐描述')
    detail = UEditorField(verbose_name=u'音乐详情', width=600, height=300, imagePath="music/ueditor/",
                          filePath="music/ueditor/", default='')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='music/%Y/%m', verbose_name=u'封面图', max_length=300)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'音乐'
        verbose_name_plural = verbose_name

    def get_music_lesson(self):
        #获取课程章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    music = models.ForeignKey(Music, verbose_name=u'音乐名')
    lesson_name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def get_lesson_lessonmusic(self):
        #获取章节音乐
        return self.lessonmusic_set.all()

    def __unicode__(self):
        return self.name


class LessonMusic(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节')
    lessonMusic_name = models.CharField(max_length=100, verbose_name=u'音乐名称')
    lrc = models.TextField(verbose_name=u'歌词', default='')
    singer = models.CharField(default='', max_length=100, verbose_name=u'歌手名字')
    music_image = models.ImageField(default='', upload_to='music/%Y/%m', verbose_name=u'封面图', max_length=300)
    music_url = models.FileField(default='', upload_to='music/resource/%Y/%m', verbose_name=u'音乐文件', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'音乐文件'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


