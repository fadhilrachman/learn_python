from django.urls import path
from .views import PostList,PostDetail,PostListForUser

urlpatterns = [
    path('admin/', PostList.as_view(), name='post-list'),
    path('admin/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('user/', PostListForUser.as_view(), name='post-list-user'),
]