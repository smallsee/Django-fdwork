# _*_ coding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import  xadmin
from django.views.static import serve


from users.views import IndexView, LoginView, RegisterView, LogoutView, ActiveUserView
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),

    #配置验证码
    url(r'^captcha/', include('captcha.urls')),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    #配置静态文件的访问处理函数
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    #视频作品url配置
    url(r'^movie/', include('movies.urls', namespace='movie')),

    #本子url配置
    url(r'^book/', include('book.urls', namespace='book')),

    #音乐url配置
    url(r'^music/', include('music.urls', namespace='music')),
    #资源url配置
    url(r'^resource/', include('resource.urls', namespace='resource')),

    #用户中心url配置
    url(r'^user/', include('users.urls', namespace='user')),

    #文章url配置
    url(r'^article/', include('article.urls', namespace='article')),

    #富文本相关
    url(r'^ueditor/', include('DjangoUeditor.urls')),

]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
