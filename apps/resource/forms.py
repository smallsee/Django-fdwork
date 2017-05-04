# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/26 23:13'
from django import forms
from captcha.fields import CaptchaField
from userdone.models import UserComments

from .models import Resource


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['image']


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'desc', 'detail', 'tag', 'resource_url']


