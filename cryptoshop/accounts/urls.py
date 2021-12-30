from .views import CustomLoginView, CustomPasswordChangeView, Controls
from django.contrib.auth.views import LogoutView, PasswordChangeView
#from django.contrib import admin
from django.urls import path, include



urlpatterns = [
	path('login', CustomLoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change_password', CustomPasswordChangeView.as_view(), name='change_password'),
	path('controls', Controls.as_view(), name='controls'),
    path('', include('viewer.urls'))

]