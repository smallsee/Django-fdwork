# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.urlresolvers import reverse

from .serializers import ArticleSerializer
from .models import Article
from userdone.models import UserComments, UserFavorite
from userdone.serializers import CommentsSerializer
from utils.mixin_utils import LoginRequiredMixin
from .forms import ArticleForm, UploadImageForm
# Create your views here.


class ArticleListView(APIView):
    def get(self, request, format=None):
        article_list = Article.objects.all()[:8]
        comment_list = UserComments.objects.filter(comments_type=int(4))

        # article_serializer = ArticleSerializer(article_list, many=True).data
        # comment_serializer = CommentsSerializer(comment_list, many=True).data
        #
        # article_ss = []
        # for article in article_serializer:
        #     article_ss.append(article)
        #     for comment in comment_serializer:
        #         if article['id'] == comment['comments_id']:
        #             article['comments'] = comment
        #
        #
        #
        # return Response({
        #     'article': article_ss,
        #     'comment': comment_serializer
        # })
        tag = request.GET.get('tag', '')
        if tag:
            article_list = Article.objects.filter(tag=tag)[:8]

        article_comment = []
        for article in article_list:
            article_comment.append(article)
            article.comments = []
            article_comment_count = 0
            article.article_comment_count = article_comment_count
            for comment in comment_list:
                if article.id == comment.comments_id:
                    article_comment_count += 1
                    article.article_comment_count = article_comment_count
                    article.comments.append(comment)

        return render(request, "articlelist.html", {
            'article_comment': article_comment,
            'tag': tag
        })


class ArticleDetailView(View):
    def get(self, request, article_id):
        ishide = True
        article = Article.objects.get(id=int(article_id))
        article.click_nums += 1
        article.save()

        has_fav_article = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=article.id, fav_type=4):
                has_fav_article = True

        #评论人员
        comment_list = UserComments.objects.filter(comments_type=int(4), comments_id=int(article_id)).order_by('-add_time')

        if request.user.id:
            comment_list_user = UserComments.objects.filter(comments_type=int(4), comments_id=int(article_id), user_id=int(request.user.id))
            if comment_list_user:
                ishide = False

        return render(request, "articledetail.html", {
            'article': article,
            'comment_list': comment_list,
            'ishide': ishide,
            'has_fav_article': has_fav_article
        })


class ArticleAddView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "articleadd.html", {})
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        article_form = ArticleForm(request.POST)
        if image_form.is_valid():
            if article_form.is_valid():
                image = image_form.cleaned_data['image']
                name = request.POST.get('name', '')
                desc = request.POST.get('desc', '')
                tag = request.POST.get('tag', '')
                detail = request.POST.get('detail', '')
                article = Article()
                article.user_id = request.user.id
                article.name = name
                article.tag = tag
                article.desc = desc
                article.detail = detail
                article.image = image
                article.save()
                return HttpResponseRedirect(reverse("article:article_list"))
            else:
                return render(request, "articleadd.html", {'article_form': article_form})
        else:
            return render(request, "articleadd.html", {'image_form': image_form})
