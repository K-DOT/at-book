# coding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()  #функция автоматического обнаружения файлов admin.py в наших приложениях

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)), #URL админки http://имя_сайта/admin/
    url(r'^blog/', include('blog.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^about/$', 'blog.views.about'),
    url(r'^$', 'blog.views.index'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/home/ruben/projects/env/bin/tamersen/tamersen/media'}),
    url(r'^how-to-buy/$', 'blog.views.htb'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
)