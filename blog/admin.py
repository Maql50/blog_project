# coding:utf-8
from django.contrib import admin
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
    #fields = ('title', 'desc', 'content')
    #exclude = ('title', 'desc', 'content')
    list_display = ('title', 'desc', 'date_publish')
    list_display_links = ('title', 'desc', 'date_publish')

    # 富文本
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

#  注册Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
#admin.site.register(Article)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

