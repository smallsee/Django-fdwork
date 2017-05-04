# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

import uuid
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
from utils.mixin_utils import LoginRequiredMixin
import qiniu.config
from forms import UploadImageForm, MovieForm, VideoForm
from models import Movies, Video
from userdone.models import UserComments, UserFavorite

# Create your views here.


class MovieListView(View):
    def get(self, request):
        #获取点击数最多并且是轮播的视频
        banner_movie = Movies.objects.filter(is_banner=True).order_by('-click_nums')[:8]
        #获取动画视频数据
        dh_movie = Movies.objects.filter(category='dh').order_by('-add_time')[:10]
        dh_movie_top = Movies.objects.filter(category='dh').order_by('-click_nums')[:7]
        # 获取番剧视频数据
        fj_movie = Movies.objects.filter(category='fj').order_by('-add_time')[:10]
        fj_movie_top = Movies.objects.filter(category='fj').order_by('-click_nums')[:7]
        # 获取鬼畜视频数据
        gc_movie = Movies.objects.filter(category='gc').order_by('-add_time')[:10]
        gc_movie_top = Movies.objects.filter(category='gc').order_by('-click_nums')[:7]
        # 获取科技视频数据
        kj_movie = Movies.objects.filter(category='kj').order_by('-add_time')[:10]
        kj_movie_top = Movies.objects.filter(category='kj').order_by('-click_nums')[:7]
        # 获取电视剧视频数据
        dsj_movie = Movies.objects.filter(category='dsj').order_by('-add_time')[:10]
        dsj_movie_top = Movies.objects.filter(category='dsj').order_by('-click_nums')[:7]
        # 获取里番视频数据
        lf_movie = Movies.objects.filter(category='lf').order_by('-add_time')[:10]
        lf_movie_top = Movies.objects.filter(category='lf').order_by('-click_nums')[:7]
        return render(request, "movielist.html", {
            'banner_movie': banner_movie,
            'dh_movie': dh_movie,
            'dh_movie_top': dh_movie_top,
            'fj_movie': fj_movie,
            'fj_movie_top': fj_movie_top,
            'gc_movie': gc_movie,
            'gc_movie_top': gc_movie_top,
            'kj_movie': kj_movie,
            'kj_movie_top': kj_movie_top,
            'dsj_movie': dsj_movie,
            'dsj_movie_top': dsj_movie_top,
            'lf_movie': lf_movie,
            'lf_movie_top': lf_movie_top
        })


class MovieDetailView(View):
    def get(self, request, movie_id):
        #找到需要的视频
        movie = Movies.objects.get(id=int(movie_id))

        has_fav_movie = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=movie.id, fav_type=1):
                has_fav_movie = True


        #是视频下的章节
        lesson_list = Video.objects.filter(movie=movie)
        #获取有多少章节
        lesson_count = Video.objects.filter(movie=movie).count()

        #获取视频
        video_id = int(request.GET.get('video_id', 0))
        video_url = lesson_list[int(video_id)]

        #评论人员
        comment_list = UserComments.objects.filter(comments_type=int(1), comments_id=int(movie_id)).order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(comment_list, 10, request=request)
        comment = p.page(page)

        return render(request, "moviedetail.html", {
            'movie': movie,
            'comment_list': comment,
            'lesson_list': lesson_list,
            'lesson_count': lesson_count,
            'video_id': video_id,
            'video_url': video_url,
            'has_fav_movie': has_fav_movie
        })


class MovieAddView(LoginRequiredMixin, View):
    def get(self, request):
        # 需要填写你的 Access Key 和 Secret Key
        access_key = '-xpzbXEV0gDocV0_SsQFn-WYczH9kPQr27wtYQ_2'
        secret_key = 'Lpynlw9BBhexmODsMV0a4-v-Kzp6zm_njdXaTUxJ'
        # 构建鉴权对象
        q = Auth(access_key, secret_key)
        # 要上传的空间
        bucket_name = 'django-fdwork'
        # 上传到七牛后保存的文件名
        key = str(uuid.uuid1()).replace('-', '')
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        return render(request, "movideadd.html", {
            'token': token,
            'key': key
        })
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        movie_form = MovieForm(request.POST)
        if image_form.is_valid():
            if movie_form.is_valid():
                image = image_form.cleaned_data['image']
                name = request.POST.get('name', '')
                desc = request.POST.get('desc', '')
                detail = request.POST.get('detail', '')
                category = request.POST.get('category', '')
                movie = Movies()
                movie.user_id = request.user.id
                movie.name = name
                movie.desc = desc
                movie.detail = detail
                movie.image = image
                movie.category = category
                movie.save()
                video_form = VideoForm(request.POST)
                if video_form:
                    url = request.POST.get('url', '')
                    video_name = request.POST.get('video_name', '')
                    video = Video()
                    video.video_name = video_name
                    video.url = url
                    video.movie = movie
                    video.save()
                    return HttpResponseRedirect(reverse("movie:movie_list"))
                else:
                    return render(request, "movideadd.html", {'video_form': video_form})
            else:
                return render(request, "movideadd.html", {'movie_form': movie_form})
        else:
            return render(request, "movideadd.html", {'image_form': image_form})
