# coding: utf-8
from blog.models import Post, Category
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response, render

def htb(request):
    return render_to_response('blog/how-t-b.html')


def about(request):
    return render_to_response('blog/about.html')

def index(request):
    return render_to_response('blog/index.html')

class PostsListView(ListView): # представление в виде списка
    model = Post
    paginate_by = 5                 # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Post


def category(request, id): # получаем аргумент id
    # делаем выборку выбранной категории
    category = Category.objects.select_related().get(id=id)
    # выбираем все статьи по выбранной категории
    posts = category.post_set.all()
    # возвращаем выбранную категорию и статьи в шаблон category.html
    return render(request, 'blog/category.html', {'posts': posts,
                                            'category': category})