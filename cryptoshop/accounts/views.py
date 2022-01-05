from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, reverse_lazy, LogoutView, PasswordChangeView
from django.views.generic import ListView, TemplateView, CreateView, DeleteView
from .forms import UserCreationForm, CreateUserForm, User
from .models import Customer
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Q
from .decorators import unauthenticated_user
# Create your views here.


def customer_registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('index')
    context = {'form': form}
    return render(request, 'signup.html', context)

def account_view(request):

    context = {}
    return render(request, 'account.html', context)


def customer_list_view(request):
    customer = Customer.objects.filter(user__groups__name='customer')
    premium = Customer.objects.filter(user__groups__name='premium')
    context = {'customer': customer, 'premium': premium}
    return render(request, 'customercontrol.html', context)

def staff_list_view(request):
    staff = Customer.objects.filter(user__groups__name='staff')
    context = {'staff': staff}
    return render(request, 'staffcontrol.html', context)

class CustomLoginView(LoginView):
    template_name = 'forms.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'forms.html'
    success_url = reverse_lazy('index')

class Controls(TemplateView):
    template_name = 'controls.html'

class UserDeleteView(DeleteView):
    template_name = 'delete_form.html'
    model = Customer
    success_url = reverse_lazy('controls')