#coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from blog.views import PostsListView, PostDetailView

urlpatterns = patterns('blog.views',


url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/books/
                                               # будет выводиться список постов

url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/books/число/
                                  # будет выводиться пост с определенным номером

url(r'^category/(?P<id>\d+)$', 'category', name="url_category"),
url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
)

