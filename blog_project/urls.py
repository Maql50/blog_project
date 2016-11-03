# coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from blog.upload import upload_image
from django.conf import settings

urlpatterns = [
    # (?P<path>.*)表示任意的字符都可以
    url(r"^uploads/(?P<path>.*)$",
        "django.views.static.serve",  # 处理静态文件
        {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
]
