# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-12 11:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userdone', '0002_articlecomments_bookcomments_moivecomments_musiccomments_userarticle_userbook_userfavorite_usermessa'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comments', models.IntegerField(choices=[(1, '\u89c6\u9891\u8bc4\u8bba'), (2, '\u97f3\u4e50\u8bc4\u8bba'), (3, '\u672c\u5b50\u8bc4\u8bba'), (4, '\u6587\u7ae0\u8bc4\u8bba')], default=1, verbose_name='\u8bc4\u8bba\u7c7b\u578b')),
                ('comments', models.CharField(max_length=200, verbose_name='\u8bc4\u8bba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u89c6\u9891\u8bc4\u8bba',
                'verbose_name_plural': '\u89c6\u9891\u8bc4\u8bba',
            },
        ),
        migrations.RemoveField(
            model_name='articlecomments',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlecomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bookcomments',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookcomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='moivecomments',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='moivecomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='musiccomments',
            name='music',
        ),
        migrations.RemoveField(
            model_name='musiccomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userarticle',
            name='article',
        ),
        migrations.RemoveField(
            model_name='userarticle',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='userbook',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usermovie',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='usermovie',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usermusic',
            name='music',
        ),
        migrations.RemoveField(
            model_name='usermusic',
            name='user',
        ),
        migrations.DeleteModel(
            name='ArticleComments',
        ),
        migrations.DeleteModel(
            name='BookComments',
        ),
        migrations.DeleteModel(
            name='MoiveComments',
        ),
        migrations.DeleteModel(
            name='MusicComments',
        ),
        migrations.DeleteModel(
            name='UserArticle',
        ),
        migrations.DeleteModel(
            name='UserBook',
        ),
        migrations.DeleteModel(
            name='UserMovie',
        ),
        migrations.DeleteModel(
            name='UserMusic',
        ),
    ]
