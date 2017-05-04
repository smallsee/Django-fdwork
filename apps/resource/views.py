# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from .models import Resource
from .forms import UploadImageForm, ResourceForm
from utils.mixin_utils import LoginRequiredMixin
from userdone.models import UserComments, UserFavorite
# Create your views here.


class ResourceListView(View):
    def get(self, request):
        resource_list = Resource.objects.all().order_by('-add_time')
        #分页处理

        # 本子筛选
        tag = request.GET.get('tag', '')
        if tag:
            resource_list = resource_list.filter(tag=tag).order_by('-add_time')

        #本子排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == "hot":
                resource_list = resource_list.order_by('-click_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(resource_list, 10, request=request)
        resource = p.page(page)
        return render(request, "resourcelist.html", {
            'resource_list': resource,
            'tag': tag,
            'sort': sort
        })


class ResourceDetailView(View):
    def get(self, request, resource_id):
        ishide = True
        resource = Resource.objects.get(id=int(resource_id))
        resource.click_nums += 1
        resource.save()

        has_fav_book = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=resource.id, fav_type=5):
                has_fav_book = True


        #评论人员
        comment_list = UserComments.objects.filter(comments_type=int(5), comments_id=int(resource_id)).order_by('-add_time')

        if request.user.id:
            comment_list_user = UserComments.objects.filter(comments_type=int(5), comments_id=int(resource_id), user_id=int(request.user.id))
            if comment_list_user:
                ishide = False

        return render(request, "resourcedetail.html", {
            'resource': resource,
            'comment_list': comment_list,
            'ishide': ishide,
            'has_fav_book': has_fav_book
        })


class ResourceAddView(View):
    def get(self, request):
        return render(request, 'resourceadd.html', {})
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        resource_form = ResourceForm(request.POST)
        if image_form.is_valid():
            if resource_form.is_valid():
                image = image_form.cleaned_data['image']
                name = request.POST.get('name', '')
                desc = request.POST.get('desc', '')
                tag = request.POST.get('tag', '')
                detail = request.POST.get('detail', '')
                resource_url = request.POST.get('resource_url', '')
                resource = Resource()
                resource.user_id = request.user.id
                resource.name = name
                resource.tag = tag
                resource.desc = desc
                resource.detail = detail
                resource.image = image
                resource.resource_url = resource_url
                resource.save()
                return HttpResponseRedirect(reverse("resource:resource_list"))
            else:
                return render(request, "resourceadd.html", {'resource_form': resource_form})
        else:
            return render(request, "resourceadd.html", {'image_form': image_form})








