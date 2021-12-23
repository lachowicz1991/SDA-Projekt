from django.urls import path

from . import views

from .views import IndexView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('news', views.home, name='home')
]