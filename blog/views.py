import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger("blog.views")

def global_setting(requests):
    return {
                'SITE_NAME': settings.SITE_NAME,
                'SITE_DESC': settings.SITE_DESC,
            }

def index(request):
    try:
        10/0
    except Exception as e:
        logger.error(e)
        logger.debug(e)
    return render(request, 'index.html', locals())