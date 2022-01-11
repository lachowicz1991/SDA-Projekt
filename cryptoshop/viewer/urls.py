from django.urls import path

from .views import IndexView, FaqView, FaqCreateView, FaqUpdateView, FaqDeleteView, FaqDetailView, \
    AdvertView, AdvertCreateView, AdvertDetailView, AdvertUpdateView, AdvertDeleteView, news


urlpatterns = [
    path('news', news, name='news'),
    path('', IndexView.as_view(), name='index'),
    path('advert', AdvertView.as_view(), name='advert'),
    path('advert/new', AdvertCreateView.as_view(), name='advert-create'),
    path('advert/<slug:slug>', AdvertDetailView.as_view(), name='advert-detail'),
    path('advert/<slug:slug>/edit', AdvertUpdateView.as_view(), name='advert-update'),
    path('advert/<slug:slug>/delete', AdvertDeleteView.as_view(), name='advert-delete'),
    path('faq', FaqView.as_view(), name='faq'),
    path('faq/new', FaqCreateView.as_view(), name='faq-create'),
    path('faq/<slug:slug>', FaqDetailView.as_view(), name='faq-detail'),
    path('faq/<slug:slug>/edit', FaqUpdateView.as_view(), name='faq-update'),
    path('faq/<slug:slug>/delete', FaqDeleteView.as_view(), name='faq-delete'),
]