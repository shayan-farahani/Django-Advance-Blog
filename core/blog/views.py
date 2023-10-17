from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post
# Create your views here.

class IndexView(TemplateView):
    """
    a class based for show index page
    """
    template_name = 'index.html'

class PostList(ListView):
    """
    this class for show list blog
    """
    queryset = Post.objects.all()
    ordering = '-id'
    paginate_by = 3
    context_object_name = 'posts'
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetail(DetailView):
    model = Post

class PostCreatedView(CreateView):
    model = Post
    fields = ['author', 'image', 'title', 'content', 'status', 'category', 'published_date']
    success_url = '/blog/'

