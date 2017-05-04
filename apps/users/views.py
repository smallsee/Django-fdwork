# _*_ coding:utf-8 _*_
import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse


from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, CommitForm
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin
from userdone.models import UserComments, UserFavorite
from movies.models import Movies
from article.models import Article
from book.models import Book
from music.models import Music
from resource.models import Resource


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    """
    首页就对了
    """
    def get(self, request):
        #热门视频
        movie_list = Movies.objects.all().order_by('-click_nums')[:5]
        # 热门本子
        book_list = Book.objects.all().order_by('-add_time')[:5]
        # 热门文章
        article_list = Article.objects.all().order_by('-click_nums')[:4]

        #首页轮播

        movie_banner = Movies.objects.all().order_by('-add_time')[:3]
        article_banner = Article.objects.all().order_by('-add_time')[:3]
        book_banner = Book.objects.all().order_by('-add_time')[:3]

        count = 0
        for movie in movie_banner:
            movie.article = article_banner[count]
            movie.book = book_banner[count]
            count += 1

        return render(request, 'index.html', {
            'movie_list': movie_list,
            'book_list': book_list,
            'article_list': article_list,
            'movie_banner': movie_banner,
        })


class LoginView(View):
    """
    登录页面
    """
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg": "账号没有激活！"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class RegisterView(View):
    """
    注册页面
    """
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {'msg': "用户已经存在", 'register_form': register_form})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {'register_form': register_form})


class ActiveUserView(View):
    """
    邮箱验证
    """
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, "login.html")


class UserCenterListView(View):
    """
    用户中心
    """
    def get(self, request, user_id):
        category = 'home'
        user_info = UserProfile.objects.get(id=int(user_id))

        #寻找用户下的本子资源
        book_user = Book.objects.filter(user=user_info)[:8]
        # 寻找用户下的视频资源
        movie_user = Movies.objects.filter(user=user_info)[:8]
        # 寻找用户下的文章资源
        article_user = Article.objects.filter(user=user_info)[:8]
        # 寻找用户下的资源
        resource_user = Resource.objects.filter(user=user_info)[:8]
        # 寻找用户下的音乐资源
        music_user = Music.objects.filter(user=user_info)[:8]

        return render(request, "usercenter-list.html", {
            'user_info': user_info,
            'book_user': book_user,
            'movie_user': movie_user,
            'music_user': music_user,
            'resource_user': resource_user,
            'article_user': article_user,
            'category': category
        })


class UserCenterCollectView(View):
    """
    用户中心
    """
    def get(self, request, user_id):

        #判断是否是自己
        if int(user_id) != request.user.id:
            return HttpResponseRedirect(reverse("index"))

        category = 'collect'
        user_info = UserProfile.objects.get(id=int(user_id))

        book_collect = UserFavorite.objects.filter(fav_type=3, user_id=int(user_id))
        movie_collect = UserFavorite.objects.filter(fav_type=1, user_id=int(user_id))
        article_collect = UserFavorite.objects.filter(fav_type=4, user_id=int(user_id))
        music_collect = UserFavorite.objects.filter(fav_type=2, user_id=int(user_id))
        resource_collect = UserFavorite.objects.filter(fav_type=5, user_id=int(user_id))

        book_collect_list = []
        movie_collect_list = []
        article_collect_list = []
        music_collect_list = []
        resource_collect_list = []

        for book_org in book_collect:
            book_org_id = book_org.fav_id
            org = Book.objects.get(id=book_org_id)
            book_collect_list.append(org)

        for movie_org in movie_collect:
            movie_org_id = movie_org.fav_id
            org = Movies.objects.get(id=movie_org_id)
            movie_collect_list.append(org)

        for article_org in article_collect:
            article_org_id = article_org.fav_id
            org = Article.objects.get(id=article_org_id)
            article_collect_list.append(org)

        for music_org in music_collect:
            music_org_id = music_org.fav_id
            org = Music.objects.get(id=music_org_id)
            music_collect_list.append(org)

        for resource_org in resource_collect:
            resource_or_id = resource_org.fav_id
            org = Resource.objects.get(id=resource_or_id)
            resource_collect_list.append(org)

        return render(request, "usercenter-collect.html", {
            'user_info': user_info,
            'book_user': book_collect_list,
            'movie_user': movie_collect_list,
            'article_user': article_collect_list,
            'music_user': music_collect_list,
            'resource_user': resource_collect_list,
            'category': category
        })



class UserCenterMovieView(View):
    """
    用户视频中心
    """
    def get(self, request, user_id):
        category = 'movie'
        user_info = UserProfile.objects.get(id=int(user_id))
        movie_user = Movies.objects.filter(user=user_info)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(movie_user, 16, request=request)
        movie = p.page(page)

        return render(request, "usercenter-movie.html", {
            'user_info': user_info,
            'movie_user': movie,
            'category': category
        })


class UserCenterBookView(View):
    """
    用户本子中心
    """
    def get(self, request, user_id):
        category = 'book'
        user_info = UserProfile.objects.get(id=int(user_id))
        book_user = Book.objects.filter(user=user_info)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(book_user, 16, request=request)
        book = p.page(page)

        return render(request, "usercenter-book.html", {
            'user_info': user_info,
            'book_user': book,
            'category': category
        })


class UserCenterArticleView(View):
    """
    用户文章中心
    """
    def get(self, request, user_id):
        category = 'article'
        user_info = UserProfile.objects.get(id=int(user_id))
        article_user = Article.objects.filter(user=user_info)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_user, 16, request=request)
        article = p.page(page)

        return render(request, "usercenter-article.html", {
            'user_info': user_info,
            'article_user': article,
            'category': category
        })


class UserCenterMusiceView(View):
    """
    用户音乐中心
    """
    def get(self, request, user_id):
        category = 'music'
        user_info = UserProfile.objects.get(id=int(user_id))
        music_user = Music.objects.filter(user=user_info)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(music_user, 16, request=request)
        music = p.page(page)

        return render(request, "usercenter-music.html", {
            'user_info': user_info,
            'music_user': music,
            'category': category
        })


class UserCenterResourceView(View):
    """
    用户资源中心
    """
    def get(self, request, user_id):
        category = 'resource'
        user_info = UserProfile.objects.get(id=int(user_id))
        resource_user = Resource.objects.filter(user=user_info)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(resource_user, 16, request=request)
        resource = p.page(page)

        return render(request, "usercenter-resource.html", {
            'user_info': user_info,
            'resource_user': resource,
            'category': category
        })


class AddCommitsView(LoginRequiredMixin, View):
    def post(self, request):
        print 'sadsa'
        commit_form = CommitForm(request.POST)
        if commit_form.is_valid():
            comments = request.POST.get('comments', '')
            comments_type = request.POST.get('comments_type', '')
            comments_id = request.POST.get('comments_id', '')
            commit = UserComments()
            commit.comments = comments
            commit.comments_type = int(comments_type)
            commit.comments_id = int(comments_id)
            commit.user_id = request.user.id
            commit.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class AddFavView(View):
    #用户收藏
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            exist_records.delete()
            if int(fav_type) == 1:
                movie = Movies.objects.get(id=int(fav_id))
                movie.fav_nums -= 1
                if movie.fav_nums < 0:
                    movie.fav_nums = 0
                movie.save()
            elif int(fav_type) == 2:
                music = Music.objects.get(id=int(fav_id))
                music.fav_nums -= 1
                if music.fav_nums < 0:
                    music.fav_nums = 0
                music.save()
            elif int(fav_type) == 3:
                book = Book.objects.get(id=int(fav_id))
                book.fav_nums -= 1
                if book.fav_nums < 0:
                    book.fav_nums = 0
                book.save()
            elif int(fav_type) == 4:
                article = Article.objects.get(id=int(fav_id))
                article.fav_nums -= 1
                if article.fav_nums < 0:
                    article.fav_nums = 0
                article.save()
            elif int(fav_type) == 5:
                resource = Resource.objects.get(id=int(fav_id))
                resource.fav_nums -= 1
                if resource.fav_nums < 0:
                    resource.fav_nums = 0
                resource.save()
            return HttpResponse('{"status":"fail", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    movie = Movies.objects.get(id=int(fav_id))
                    movie.fav_nums += 1
                    movie.save()
                elif int(fav_type) == 2:
                    music = Music.objects.get(id=int(fav_id))
                    music.fav_nums += 1
                    music.save()
                elif int(fav_type) == 3:
                    book = Book.objects.get(id=int(fav_id))
                    book.fav_nums += 1
                    book.save()
                elif int(fav_type) == 4:
                    article = Article.objects.get(id=int(fav_id))
                    article.fav_nums += 1
                    article.save()
                elif int(fav_type) == 5:
                    resource = Resource.objects.get(id=int(fav_id))
                    resource.fav_nums += 1
                    resource.save()

                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')










def page_not_found(request):
    #全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    #全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response



# Create your views here.
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误！"})
#     elif request.method == "GET":
#         return render(request, "login.html", {})
