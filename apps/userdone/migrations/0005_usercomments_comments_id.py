# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-15 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdone', '0004_auto_20170415_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomments',
            name='comments_id',
            field=models.IntegerField(default=0, verbose_name='\u6570\u636eid'),
        ),
    ]