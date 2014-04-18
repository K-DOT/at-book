# coding: utf-8
from django.contrib import admin

from django.contrib import admin
from blog.models import Post, Category # наша модель из books/models.py

admin.site.register(Post)
admin.site.register(Category)
