from .views import CustomLoginView, CustomPasswordChangeView, Controls, UserDeleteView, customer_registration,staff_list_view, customer_list_view
from django.contrib.auth.views import LogoutView, PasswordChangeView
# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change_password', CustomPasswordChangeView.as_view(), name='change_password'),
	path('controls', Controls.as_view(), name='controls'),
	path('signup', customer_registration, name='signup'),
	path('customercontrol', customer_list_view, name='customercontrol'),
	path('staffcontrol', staff_list_view, name='staffcontrol'),
	path('<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),
	path('', include('viewer.urls'))
]
