# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-26 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdone', '0006_auto_20170420_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomments',
            name='comments_type',
            field=models.IntegerField(choices=[(1, '\u89c6\u9891\u8bc4\u8bba'), (2, '\u97f3\u4e50\u8bc4\u8bba'), (3, '\u672c\u5b50\u8bc4\u8bba'), (4, '\u6587\u7ae0\u8bc4\u8bba'), (5, '\u8d44\u6e90\u8bc4\u8bba')], default=1, verbose_name='\u8bc4\u8bba\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '\u89c6\u9891'), (2, '\u97f3\u4e50'), (3, '\u672c\u5b50'), (4, '\u6587\u7ae0'), (5, '\u8d44\u6e90')], default=1, verbose_name='\u6536\u85cf\u7c7b\u578b'),
        ),
    ]
