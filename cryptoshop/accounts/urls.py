from .views import CustomLoginView, CustomPasswordChangeView, Controls, CustomPasswordResetView,\
	CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

from django.contrib.auth.views import LogoutView
#from django.contrib import admin
from django.urls import path



urlpatterns = [
	path('login', CustomLoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change_password', CustomPasswordChangeView.as_view(), name='change_password'),
	path("password-reset", CustomPasswordResetView.as_view(), name="password_reset"),
	path("password-reset/done/", CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
	path("password-reset-confirm/<uidb64>/<token>",CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
	path("password-reset-complete/", CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
	path('controls', Controls.as_view(), name='controls'),
]