from django.shortcuts import render
from django.contrib.auth.views import LoginView, reverse_lazy, LogoutView, PasswordChangeView
from django.views.generic import ListView, TemplateView
from .models import Customer
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'forms.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'forms.html'
    success_url = reverse_lazy('index')


class CustomerListView(ListView):
    template_name = 'gear.html'
    model = Customer
    context_object_name = 'gear'

class Controls(TemplateView):
    template_name = 'controls.html'
