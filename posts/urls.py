from django.urls import path
from .views import (HomeView,PostCreateview,PostsListView)
app_name = 'posts'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('create_post/',PostCreateview.as_view(),name='create_post'),
    path('list_posts/',PostsListView.as_view(),name='list_posts'),
]
