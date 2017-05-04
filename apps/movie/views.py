from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class MovieListView(View):
    def get(self, request):
        return render(request, "movielist.html", {})


class MovieDetailView(View):
    def get(self, request):
        return render(request, "moviedetail.html", {})
