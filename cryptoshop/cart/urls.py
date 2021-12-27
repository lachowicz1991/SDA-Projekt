from django.contrib import admin
from django.urls import path, include
from .views import cart, checkout, updateItem, processOrder, store, CourseDetailView, ProductCreateView,\
	ProductDeleteView, ProductUpdateView

urlpatterns = [
	path('store/', store, name='store'),
	path('cart/', cart, name='cart'),
	path('checkout/', checkout, name='checkout'),
	path('update_item/', updateItem, name='update_item'),
	path('process_order/', processOrder, name='process_order'),
	path('product_detail/<int:pk>', CourseDetailView.as_view(), name='product_detail'),
	path('product_detail/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
	path('product_detail/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
	path('store/create', ProductCreateView.as_view(), name='product-create'),
]
