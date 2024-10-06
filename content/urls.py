from django.urls import path
from .views import ContentListForAdmin, ContentDetailForAdmin, ContentListForUser

urlpatterns = [
    path('user/', ContentListForUser.as_view(), name='content-list-user'),
    path('admin/', ContentListForAdmin.as_view(), name='content-list'),
    path('admin/<int:pk>/', ContentDetailForAdmin.as_view(), name='content-detail'),
]