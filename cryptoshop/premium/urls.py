from django.urls import path
from .views import CryptoView

urlpatterns = [
    path('crypto', CryptoView.as_view(), name='cryptomarket'),
]