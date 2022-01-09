from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, reverse_lazy, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
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


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password_reset_complete.html"

