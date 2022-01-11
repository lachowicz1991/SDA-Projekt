from django.urls import path

from .views import CryptoView, TechnicalAnalysis

urlpatterns = [
    path('crypto', CryptoView.as_view(), name='cryptomarket'),
    path('technical-analysis', TechnicalAnalysis.as_view(), name='technnical_analysis' )
]