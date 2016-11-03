# coding:utf8
import logging
from django.shortcuts import render
from django.conf import settings
from blog.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import  Count
logger = logging.getLogger("blog.views")

def global_setting(requests):
    archive_list = Article.objects.distinct_date()
    category_list = Category.objects.all()
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC

    comment_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_list]
    return locals()

def index(request):
    # try:
    #     10/0
    # except Exception as e:
    #     logger.error(e)
    #     logger.debug(e)
    #从数据库只取出一条
    article_list = Article.objects.all()
    page_size = 2
    article_list = getPage(request, article_list, page_size)
    #print Article.objects.values('date_publish').distinct()

    # 错误，需要主键
    # archive_list = Article.objects.raw("SELECT DISTINCT( to_char(date_publish,'yyyy-mm-dd')) as publib_date FROM blog_article ORDER BY publib_date desc;")
    # for archive in archive_list:
    #     print archive

    # 执行成功，但最后不用
    # cursor = connection.cursor()
    # cursor.execute("SELECT DISTINCT( to_char(date_publish,'yyyy-mm-dd')) as publib_date FROM blog_article ORDER BY publib_date desc;")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print row

    return render(request, 'index.html', locals())

def archive(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    # 模糊查询
    print year, month
    article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
    page_size = 2
    article_list = getPage(request, article_list, page_size)
    return render(request, 'archive.html', locals())

def article(request):
    id = request.GET.get('id')
    try:
        Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return render(request, 'failure.html', {'reason': '没有找到对应的文章'})

def getPage(request, article_list, page_size):
    pageinator = Paginator(article_list, page_size)
    try:
        page = int(request.GET.get('page', 1))
        article_list = pageinator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger) as e:
        article_list = pageinator.page(1)
    return article_list