from django.urls import path
from .views import TransactionListForAdmin, TransactionCreateForUser

urlpatterns = [
    path('admin/', TransactionListForAdmin.as_view(), name='transaction-list'),
    path('user/donation', TransactionCreateForUser.as_view(), name='transaction-create'),
]