from django.urls import path
from apps.demo.views import PostListCreateView, PostDetailView, CommentListCreateView


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<uuid:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    ]