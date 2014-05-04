# coding: utf-8
from django.contrib import admin

from django.contrib import admin
from blog.models import Post, Category # наша модель из books/models.py

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'category', 'image')
    list_filter = ('datetime',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
