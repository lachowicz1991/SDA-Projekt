from .views import CustomLoginView, CustomPasswordChangeView, Controls, UserDeleteView, customer_registration,\
	staff_list_view, customer_list_view, customer_update
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView,PasswordResetDoneView,\
	PasswordResetConfirmView, PasswordResetView
from django.urls import path, include


urlpatterns = [
	path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change_password', CustomPasswordChangeView.as_view(), name='change_password'),
	path('controls', Controls.as_view(), name='controls'),
	path('signup', customer_registration, name='signup'),
	path('customercontrol', customer_list_view, name='customercontrol'),
	path('staffcontrol', staff_list_view, name='staffcontrol'),
	path('<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),
	path('<int:id>/update', customer_update, name='user-update'),
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
