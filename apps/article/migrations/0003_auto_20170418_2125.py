# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-18 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(choices=[('jl', '\u4ea4\u6d41'), ('dhzx', '\u52a8\u753b\u8d44\u8baf'), ('qtzx', '\u5176\u4ed6\u54a8\u8be2'), ('fdsw', 'fd\u4e8b\u52a1')], default='jl', max_length=50, verbose_name='\u672c\u5b50\u7c7b\u578b'),
        ),
    ]
