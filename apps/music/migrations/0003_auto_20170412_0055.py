# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-12 00:55
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170412_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u97f3\u4e50\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='music',
            name='tag',
            field=models.CharField(choices=[('dmtj', '\u52a8\u6f2b\u56fe\u96c6'), ('zzhj', '\u6742\u5fd7\u753b\u96c6'), ('tztj', '\u5c60\u7ad9\u63a8\u8350'), ('yxcg', '\u6e38\u620fCG'), ('grzh', '\u4e2a\u4eba\u6742\u753b')], default='grzh', max_length=50, verbose_name='\u97f3\u4e50\u7c7b\u578b'),
        ),
    ]
