from django.urls import path
from .views import (PostCreateview,HomePostsListView,
                    PostDetailview,PostUpdateView,PostDeleteView,
                    SignUpCreateView)
app_name = 'posts'

# mysuperadmin = {'username' : 'admin',
#                 'password' : 'sme123',
#                 }



urlpatterns = [
    path('',HomePostsListView.as_view(),name='home'),
    path('create_post/',PostCreateview.as_view(),name='create_post'),
    # path('list_posts/',HomePostsListView.as_view(),name='list_posts'),
    path('post_detail/<int:pk>',PostDetailview.as_view(),name='detail_post'),
    path('update_post/<int:pk>',PostUpdateView.as_view(),name='post_update'),
    path('delete_post/<int:pk>',PostDeleteView.as_view(),name='delete_post'),
    path('signup/',SignUpCreateView.as_view(),name='signup')
]
