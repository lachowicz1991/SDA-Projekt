from django.shortcuts import render
from django.contrib.auth.views import LoginView, reverse_lazy, LogoutView, PasswordChangeView
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'forms.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'forms.html'
    success_url = reverse_lazy('index')


