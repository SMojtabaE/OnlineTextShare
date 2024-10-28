from django.urls import path
from .views import (PostCreateview,HomePostsListView,
                    PostDetailview,PostUpdateView,PostDeleteView,
                    SignUpCreateView,UserPostListView,PublicPostDetailview)
app_name = 'posts'

urlpatterns = [
    path('',HomePostsListView.as_view(),name='home'),
    path('create_post/',PostCreateview.as_view(),name='create_post'),
    path('list_posts/',UserPostListView.as_view(),name='list_posts'),
    path('post_detail/<int:pk>',PostDetailview.as_view(),name='detail_post'),
    path('public_post_detail/<int:pk>',PublicPostDetailview.as_view(),name='public_detail_post'),
    path('update_post/<int:pk>',PostUpdateView.as_view(),name='post_update'),
    path('delete_post/<int:pk>',PostDeleteView.as_view(),name='delete_post'),
    path('signup/',SignUpCreateView.as_view(),name='signup')
]
