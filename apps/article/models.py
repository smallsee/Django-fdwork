# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models
from users.models import UserProfile
from userdone.models import UserComments
# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'文章名')
    user = models.ForeignKey(UserProfile, verbose_name=u'发布者', default='')
    desc = models.CharField(max_length=300, verbose_name=u'文章描述')
    detail = UEditorField(verbose_name=u'文章详情', width=600, height=300, imagePath="article/ueditor/",
                          filePath="article/ueditor/", default='')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='article/%Y/%m', verbose_name=u'封面图', max_length=300)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(verbose_name=u'本子类型', max_length=50, choices=(('jl', u'交流'), ('dhzx', u'动画资讯'), ('qtzx', u'其他咨询'), ('fdsw', u'fd事务')), default='jl')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


