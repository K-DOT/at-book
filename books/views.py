# coding: utf-8
from books.models import Post
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = Post
    paginate_by = 3                 # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Post