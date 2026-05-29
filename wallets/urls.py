from django.urls import path
from .views import WalletListCreateAPIView

urlpatterns = [
    path('', WalletListCreateAPIView.as_view(), name='wallet-list-create')
]