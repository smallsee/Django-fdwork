# _*_ coding:utf-8 _*_
__author__ = 'xiaohai'
__date__ = '2017/3/26 23:13'
from django import forms
from captcha.fields import CaptchaField
from userdone.models import UserComments

from .models import Music, Lesson, LessonMusic


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['image']


class UploadMusicImageForm(forms.ModelForm):
    class Meta:
        model = LessonMusic
        fields = ['music_image']


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'desc', 'detail', 'tag']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_name']


class LessonMusicForm(forms.ModelForm):
    class Meta:
        model = LessonMusic
        fields = ['singer', 'lessonMusic_name']


