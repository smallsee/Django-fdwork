# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-15 19:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdone', '0003_auto_20170412_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomments',
            old_name='user_comments',
            new_name='comments_type',
        ),
    ]
