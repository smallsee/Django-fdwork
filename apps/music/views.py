# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from .models import Music, Lesson, LessonMusic
from .forms import LessonForm, MusicForm, UploadImageForm, LessonMusicForm, UploadMusicImageForm
from userdone.models import UserFavorite, UserComments
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

import uuid
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
from utils.mixin_utils import LoginRequiredMixin
import qiniu.config
# Create your views here.


class MusicListView(View):
    def get(self, request):
        music_list = Music.objects.all()

        # 本子筛选
        tag = request.GET.get('tag', '')
        if tag:
            music_list = music_list.filter(tag=tag).order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(music_list, 20, request=request)
        music = p.page(page)
        return render(request, 'musiclist.html', {
            'music_list': music,
            'tag': tag
        })


class MusicDetailView(View):
    def get(self, request, music_id):
        ishide = True
        music = Music.objects.get(id=int(music_id))
        music.click_nums += 1
        music.save()


        has_fav_music = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=music.id, fav_type=2):
                has_fav_music = True

        # 评论人员
        comment_list = UserComments.objects.filter(comments_type=int(2), comments_id=int(music_id)).order_by(
            '-add_time')

        if request.user.id:
            comment_list_user = UserComments.objects.filter(comments_type=int(3), comments_id=int(music_id),
                                                            user_id=int(request.user.id))
            if comment_list_user:
                ishide = False

        return render(request, 'musicdetail.html', {
            'music': music,
            'has_fav_music': has_fav_music,
            'ishide': ishide,
            'comment_list': comment_list
        })


class MusicAddView(LoginRequiredMixin, View):
    def get(self, request):
        # 需要填写你的 Access Key 和 Secret Key
        access_key = '-xpzbXEV0gDocV0_SsQFn-WYczH9kPQr27wtYQ_2'
        secret_key = 'Lpynlw9BBhexmODsMV0a4-v-Kzp6zm_njdXaTUxJ'
        # 构建鉴权对象
        q = Auth(access_key, secret_key)
        # 要上传的空间
        bucket_name = 'django-fdword-music'
        # 上传到七牛后保存的文件名
        key = str(uuid.uuid1()).replace('-', '')
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        return render(request, "musicadd.html", {
            'token': token,
            'key': key
        })
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        music_image_form = UploadMusicImageForm(request.POST, request.FILES)
        music_form = MusicForm(request.POST)
        lesson_form = LessonForm(request.POST)
        lesson_music_form = LessonMusicForm(request.POST)
        if image_form.is_valid() and music_image_form.is_valid():
            if music_form.is_valid() and lesson_form.is_valid() and lesson_music_form.is_valid():
                image = image_form.cleaned_data['image']
                print image
                name = request.POST.get('name', '')
                desc = request.POST.get('desc', '')
                detail = request.POST.get('detail', '')
                tag = request.POST.get('tag', '')
                music = Music()
                music.user_id = request.user.id
                music.name = name
                music.detail = detail
                music.tag = tag
                music.desc = desc
                music.image = image
                music.save()
                lesson_name = request.POST.get('lesson_name', '')
                lesson = Lesson()
                lesson.lesson_name = lesson_name
                lesson.music = music
                lesson.save()
                lessonMusic_name = request.POST.get('lessonMusic_name', '')
                singer = request.POST.get('singer', '')
                music_url = request.POST.get('music_url', '')
                music_image = music_image_form.cleaned_data['music_image']
                music_lesson = LessonMusic()
                music_lesson.lessonMusic_name = lessonMusic_name
                music_lesson.singer = singer
                music_lesson.music_url = music_url
                music_lesson.music_image = music_image
                music_lesson.lesson = lesson
                music_lesson.save()
                return HttpResponseRedirect(reverse("music:music_list"))

            return render(request, "musicadd.html", {'msg': "有东西出错"})
        return render(request, "musicadd.html", {'msg': "图片没有上床好呀，兄弟"})

