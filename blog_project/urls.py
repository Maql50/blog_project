# coding:utf-8
"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index
from blog.upload import upload_image
from django.conf import settings

urlpatterns = [
    # (?P<path>.*)表示任意的字符都可以
    url(r"^uploads/(?P<path>.*)$",
        "django.views.static.serve",  # 处理静态文件
        {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index, name='index'),

]
