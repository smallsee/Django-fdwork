# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from .models import Book
from .forms import UploadImageForm, BookForm
from utils.mixin_utils import LoginRequiredMixin
from userdone.models import UserComments, UserFavorite
# Create your views here.


class BookListView(View):
    def get(self, request):
        book_list = Book.objects.all().order_by('-add_time')
        #分页处理

        # 本子筛选
        tag = request.GET.get('tag', '')
        if tag:
            book_list = book_list.filter(tag=tag).order_by('-add_time')

        #本子排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == "hot":
                book_list = book_list.order_by('-click_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(book_list, 10, request=request)
        books = p.page(page)
        return render(request, "booklist.html", {
            'book_list': books,
            'tag': tag,
            'sort': sort
        })


class BookDetailView(View):
    def get(self, request, book_id):
        ishide = True
        book = Book.objects.get(id=int(book_id))
        book.click_nums += 1
        book.save()

        has_fav_book = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=book.id, fav_type=3):
                has_fav_book = True


        #评论人员
        comment_list = UserComments.objects.filter(comments_type=int(3), comments_id=int(book_id)).order_by('-add_time')

        if request.user.id:
            comment_list_user = UserComments.objects.filter(comments_type=int(3), comments_id=int(book_id), user_id=int(request.user.id))
            if comment_list_user:
                ishide = False

        return render(request, "bookdetail.html", {
            'book': book,
            'comment_list': comment_list,
            'ishide': ishide,
            'has_fav_book': has_fav_book
        })


class BookAddView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "bookadd.html", {})
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        book_form = BookForm(request.POST)
        if image_form.is_valid():
            if book_form.is_valid():
                image = image_form.cleaned_data['image']
                name = request.POST.get('name', '')
                desc = request.POST.get('desc', '')
                tag = request.POST.get('tag', '')
                book_list = request.POST.get('book_list', '')
                book = Book()
                book.user_id = request.user.id
                book.name = name
                book.tag = tag
                book.desc = desc
                book.book_list = book_list
                book.image = image
                book.save()
                return HttpResponseRedirect(reverse("book:book_list"))
            else:
                return render(request, "booklist.html", {'book_form': book_form})
        else:
            return render(request, "booklist.html", {'image_form': image_form})











