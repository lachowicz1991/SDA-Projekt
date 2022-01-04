from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, reverse_lazy, LogoutView, PasswordChangeView
from django.views.generic import ListView, TemplateView, CreateView
from .forms import UserCreationForm, CreateUserForm
from .models import Customer
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib import messages
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
    orders = req
    context = {}
    return render(request, 'account.html', context)

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
