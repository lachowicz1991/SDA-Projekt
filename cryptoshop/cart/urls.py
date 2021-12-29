from django.contrib import admin
from django.urls import path, include
from .views import cart, checkout, updateItem, processOrder, store

urlpatterns = [
    path('store/', store, name='store'),
	path('cart/', cart, name='cart'),
	path('checkout/', checkout, name='checkout'),
	path('update_item/', updateItem, name='update_item'),
	path('process_order/', processOrder, name='process_order')
]