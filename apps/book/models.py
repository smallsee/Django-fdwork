# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models
from users.models import UserProfile
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'本子名')
    user = models.ForeignKey(UserProfile, verbose_name=u'发布者', default='')
    desc = models.CharField(max_length=300, verbose_name=u'本子描述')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='book/%Y/%m', verbose_name=u'封面图', max_length=300)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(verbose_name=u'本子类型', max_length=50, choices=(('dmtj', u'动漫图集'), ('zzhj', u'杂志画集'), ('wztj', u'网站推荐'), ('yxcg', u'游戏CG'), ('grzh', u'个人杂画')), default='grzh')
    book_list = UEditorField(verbose_name=u'本子图片', width=600, height=300, imagePath="book/list/ueditor/",
                          filePath="book/list/ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'本子'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name




