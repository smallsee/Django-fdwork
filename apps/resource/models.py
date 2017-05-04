# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models
from users.models import UserProfile
# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'资源名')
    user = models.ForeignKey(UserProfile, verbose_name=u'发布者', default='')
    desc = models.CharField(max_length=300, verbose_name=u'资源描述')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='resource/%Y/%m', verbose_name=u'封面图', max_length=300)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(verbose_name=u'资源类型', max_length=50, choices=(('rj', u'软件'), ('sr', u'生肉'), ('game', u'游戏'), ('jc', u'教程'), ('qt', u'其他')), default='qt')
    detail = UEditorField(verbose_name=u'资源详情', width=600, height=300, imagePath="resource/list/ueditor/",
                          filePath="resource/list/ueditor/", default='')
    resource_url = models.TextField(default='', verbose_name=u'资源的链接（百度云盘）')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name




