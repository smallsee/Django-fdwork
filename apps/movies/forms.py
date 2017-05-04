# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/26 23:13'
from django import forms
from captcha.fields import CaptchaField
from userdone.models import UserComments

from .models import Movies, Video


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['image']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'desc', 'detail', 'category']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url', 'video_name']


