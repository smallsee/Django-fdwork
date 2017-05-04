# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-28 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170325_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u5fd8\u8bb0\u5bc6\u7801')], default='female', max_length=10, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b'),
        ),
    ]
