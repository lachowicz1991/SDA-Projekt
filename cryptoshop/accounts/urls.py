from .views import CustomLoginView,  CustomPasswordChangeView, OrderItemListView, OrderListView, Controls, UserDeleteView, customer_registration,\
	staff_list_view, customer_list_view, ProfileUpdateView, ContactView, OrderDeleteView, OrderItemDeleteView
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetDoneView,\
	PasswordResetConfirmView, PasswordResetView

from viewer.views import AdvertControlView, ArticleControlView, FaqControlView
from django.urls import path, include


urlpatterns = [
	path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change_password', CustomPasswordChangeView.as_view(), name='change_password'),
	path('controls', Controls.as_view(), name='controls'),
	path('contact', ContactView.as_view(), name='contact'),
	path('signup', customer_registration, name='signup'),
	path('<int:pk>/orders', OrderItemListView.as_view(), name='orders'),
	path('order-list', OrderListView.as_view(), name='order_list'),
	path('advert-control', AdvertControlView.as_view(), name='advert-control'),
	path('article-control', ArticleControlView.as_view(), name='article-control'),
	path('faq-control', FaqControlView.as_view(), name='faq-control'),
	path('customercontrol', customer_list_view, name='customercontrol'),
	path('staffcontrol', staff_list_view, name='staffcontrol'),
	path('<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),
	path('<int:pk>/update', ProfileUpdateView.as_view(), name='user-update'),
	path('<int:pk>/delete_order', OrderDeleteView.as_view(), name='order-delete'),
	path('<int:pk>/delete_order', OrderDeleteView.as_view(), name='order-delete'),
	path('<int:pk>/delete_order', OrderItemDeleteView.as_view(), name='orderitem-delete'),

	path('', include('viewer.urls')),
	path('reset_password/',
		 PasswordResetView.as_view(template_name="password_reset.html"),
		 name="reset_password"),
	path('reset_password_sent/',
		 PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
		 name="password_reset_done"),
	path('reset/<uidb64>/<token>/',
		 PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
		 name="password_reset_confirm"),
	path('reset_password_complete/',
		 PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
		 name="password_reset_complete"),
]
