from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'posts/index.html'

#     context_object_name = 'posts_list'
#     def get_queryset(self):
#         return Post.objects.filter(is_publick=True)
    

class PostCreateview(LoginRequiredMixin,CreateView):           # templat = > post_form.html
    model = Post
    fields = ['title','content','is_publick']

    success_url = reverse_lazy('posts:list_posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HomePostsListView(ListView):   #home page           # template = > index.html
    model = Post
    template_name = 'posts/index.html'

    context_object_name = 'posts_list'
    def get_queryset(self):
        return Post.objects.filter(is_publick=True)
    
class UserPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        if self.request.user.is_staff:           # check if superuser is logedtn, show all posts
            return Post.objects.all()
        
        return Post.objects.filter(user=self.request.user)         # if regular user,only show the users posts

class PostDetailview(LoginRequiredMixin,DetailView):           # tempalte = > post_detail.html
    model = Post

class PublicPostDetailview(DetailView):           # tempalte = > public_post_detail.html
    model = Post
    template_name = 'posts/public_post_detail.html'


class PostUpdateView(LoginRequiredMixin,UpdateView):           # template = > post_form.html    build befor
    model = Post
    fields = ['title', 'content','is_publick']
    # success_url = reverse_lazy('posts:list_posts') 
    success_url = reverse_lazy('posts:list_posts')

class PostDeleteView(LoginRequiredMixin,DeleteView):           # template = > post_confirm_delete.html
    model = Post
    # success_url = reverse_lazy('posts:list_posts')
    success_url = reverse_lazy('posts:home')

class SignUpCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'