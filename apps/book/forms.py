# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/26 23:13'
from django import forms
from captcha.fields import CaptchaField
from userdone.models import UserComments

from .models import Book


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['image']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'desc', 'book_list', 'tag']


