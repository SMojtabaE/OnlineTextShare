from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = 'posts/home.html'

class PostCreateview(LoginRequiredMixin,CreateView):           # templat = > post_form.html
    model = Post
    fields = ['title','content']

    success_url = reverse_lazy('posts:home')

class PostsListView(ListView):              # template = > post_list.html
    model = Post

    context_object_name = 'posts_list'

class PostDetailview(DetailView):           # tempalte = > post_detail.html
    model = Post
    ordering = ['date_posted']


class PostUpdateView(LoginRequiredMixin,UpdateView):           # template = > post_form.html    build befor
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('posts:list_posts')

class PostDeleteView(LoginRequiredMixin,DeleteView):           # template = > post_confirm_delete.html
    model = Post
    success_url = reverse_lazy('posts:list_posts')


class SignUpCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'