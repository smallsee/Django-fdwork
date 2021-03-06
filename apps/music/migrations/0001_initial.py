# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-11 23:54
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u97f3\u4e50\u540d')),
                ('desc', models.CharField(max_length=300, verbose_name='\u97f3\u4e50\u63cf\u8ff0')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='\u8bfe\u7a0b\u8be6\u60c5')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('image', models.ImageField(max_length=300, upload_to='music/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('music_url', models.FileField(max_length=200, upload_to='music/resource/%Y/%m', verbose_name='\u97f3\u4e50\u6587\u4ef6')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='\u97f3\u4e50\u6807\u7b7e')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u97f3\u4e50',
                'verbose_name_plural': '\u97f3\u4e50',
            },
        ),
    ]
