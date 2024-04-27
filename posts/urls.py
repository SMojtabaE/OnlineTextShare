from django.urls import path
from .views import (HomeView,PostCreateview,PostsListView,
                    PostDetailview,PostUpdateView,PostDeleteView)
app_name = 'posts'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('create_post/',PostCreateview.as_view(),name='create_post'),
    path('list_posts/',PostsListView.as_view(),name='list_posts'),
    path('post_detail/<int:pk>',PostDetailview.as_view(),name='detail_post'),
    path('update_post/<int:pk>',PostUpdateView.as_view(),name='post_update'),
    path('delete_post/<int:pk>',PostDeleteView.as_view(),name='delete_post')
]
