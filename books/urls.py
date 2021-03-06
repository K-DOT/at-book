#coding: utf-8
from django.conf.urls import patterns, url

from books.views import PostsListView, PostDetailView
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/books/
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/books/число/
url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
)