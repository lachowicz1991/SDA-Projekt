from django.contrib import admin
from django.urls import path, include
from .views import cart, checkout

urlpatterns = [
	path('cart/', cart, name='cart'),
	path('checkout/', checkout, name='checkout'),
]