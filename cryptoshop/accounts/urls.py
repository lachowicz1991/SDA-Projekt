from django.urls import path
from .views import CustomLoginView, CustomPasswordChangeView
from django.contrib.auth.views import LogoutView, PasswordChangeView
urlpatterns = [
	path('login', CustomLoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change_password', CustomPasswordChangeView.as_view(), name='change_password')
]