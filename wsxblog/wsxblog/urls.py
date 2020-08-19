"""wsxblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from blogs import views

from blogs.models import Blogs
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

info_dict = {
    'queryset': Blogs.objects.all(),
    'date_field': 'modifyed_time'
}

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^', include(('blogs.urls', "blog"), namespace='blog')),
    # re_path('^search', include('haystack.urls')),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = views.page_not_found
