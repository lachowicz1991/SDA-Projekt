from django.urls import path

from .views import IndexView, AdvertView

urlpatterns = [

    path('index', IndexView.as_view(), name='index'),
    path('adverts', AdvertView.as_view(), name='adverts')
]