from django.urls import path

from .views import CryptoView, TechnicalAnalysisView, BreakingNewsView, PredictionsView, InvestmentStrategiesView, PredictionsCreateView, \
    PredictionsDeleteView, PredictionsUpdateView, PredictionsDetailView, BreakingNewsDeleteView, BreakingNewsDetailView, \
    BreakingNewsUpdateView, BreakingNewsCreateView, InvestmentStrategiesUpdateView, InvestmentStrategiesDetailView, \
    InvestmentStrategiesCreateView, InvestmentStrategiesDeleteView

urlpatterns = [
    path('crypto', CryptoView.as_view(), name='cryptomarket'),
    path('technical-analysis', TechnicalAnalysisView.as_view(), name='technnical_analysis'),
    path('breaking-news', BreakingNewsView.as_view(), name='breaking_news'),
    path('breaking-news/new', BreakingNewsCreateView.as_view(), name='breaking_news-create'),
    path('breaking-news/<slug:slug>', BreakingNewsDetailView.as_view(), name='breaking_news-detail'),
    path('breaking-news/<slug:slug>/edit', BreakingNewsUpdateView.as_view(), name='breaking_news-update'),
    path('breaking-news/<slug:slug>/delete', BreakingNewsDeleteView.as_view(), name='breaking_news-delete'),
    path('predictions', PredictionsView.as_view(), name='prediction'),
    path('predictions/new', PredictionsCreateView.as_view(), name='prediction-create'),
    path('predictions/<slug:slug>', PredictionsDetailView.as_view(), name='prediction-detail'),
    path('predictions/<slug:slug>/edit', PredictionsUpdateView.as_view(), name='prediction-update'),
    path('predictions/<slug:slug>/delete', PredictionsDeleteView.as_view(), name='prediction-delete'),
    path('investment-strategies', InvestmentStrategiesView.as_view(), name='investment_strategies'),
    path('investment-strategies/new', InvestmentStrategiesCreateView.as_view(), name='investment_strategies-create'),
    path('investment-strategies/<slug:slug>', InvestmentStrategiesDetailView.as_view(),
         name='investment_strategies-detail'),
    path('investment-strategies/<slug:slug>/edit', InvestmentStrategiesUpdateView.as_view(),
         name='investment_strategies-update'),
    path('investment-strategies/<slug:slug>/delete', InvestmentStrategiesDeleteView.as_view(),
         name='investment_strategies-delete'),
]