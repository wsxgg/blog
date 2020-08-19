
from django.contrib import admin
from django.urls import path, re_path, include

from blogs.views import IndexView, ShowBlogView, ListView, SearchView, CommentView, NewCommentView, VlogListView, VlogDetailView
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^blog/(?P<blog_id>.+)', ShowBlogView.as_view(), name='detail'),
    re_path(r'^list/(?P<tag>.+)/(?P<page>\d+)', ListView.as_view(), name='list'),
    re_path(r'^search/(?P<page>\d+)', SearchView.as_view(), name='search'),
	re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}, name='static'),
    re_path(r'^comment/(?P<page>.*)$', CommentView.as_view(), name="comment"),
    re_path(r"^newcomment", NewCommentView.as_view(), name="newcomment"),
    re_path(r"^vlog/list/(?P<page>.*)$", VlogListView.as_view(), name="vloglist"),
    re_path(r"^vlog/(?P<vlog_id>\d+)$", VlogDetailView.as_view(), name="vlog"),
]

