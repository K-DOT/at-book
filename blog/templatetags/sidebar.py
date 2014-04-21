# -*- coding: utf-8 -*-
from django import template
from blog.models import Category, Post # импортируем модели
from django.db.models import Count

# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()
# регистрируем наш тег, который будет выводить шаблон right_sidebar.html
@register.inclusion_tag("blog/right_sidebar.html")
def show_sidebar():
    # выбираем все категории
    categories = Category.objects.all().order_by("name").annotate(count_post = Count('post'))
    # выбираем все статьи по id - для ссылок и title - для списка
    new_posts = Post.objects.values('id','title').order_by("-datetime")[:10]
    # возвращаем наши объекты в шаблон
    return { 'categories': categories, 'new_posts': new_posts}