# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/4/18 8:59'

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'desc', 'user', 'image']