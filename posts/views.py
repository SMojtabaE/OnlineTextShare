from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'posts/home.html'

class PostCreateview(CreateView):           # templat = > post_form.html
    model = Post
    fields = ['title','content']

    success_url = reverse_lazy('posts:home')

class PostsListView(ListView):              # template = > post_list.html
    model = Post

    context_object_name = 'posts_list'