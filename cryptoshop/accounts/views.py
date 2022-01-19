from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView, reverse_lazy, LogoutView, PasswordChangeView
from django.views.generic import ListView, UpdateView, DetailView, TemplateView, CreateView, DeleteView
from .forms import AdminUserUpdateForm, CreateUserForm, CreateCustomerForm
from .models import Customer
from cart.models import ShippingAddress, OrderItem, Order
from django.contrib.auth.models import Group
from django.contrib import messages
from cart.utils import cartData

# Create your views here.

def customer_registration(request):
    form = CreateUserForm()
    form2 = CreateCustomerForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = CreateCustomerForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            form2.instance.user = user
            form2.save()
            username = user.username
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, f'Account was created for {username}')
            return redirect('advert')
    context = {'form': form, 'form2': form2}
    return render(request, 'signup.html', context)

class ProfileUpdateView(UpdateView):
    template_name = 'forms.html'
    form_class = AdminUserUpdateForm
    model = Customer
    success_url = reverse_lazy('controls')

    def get_object(self, queryset=None):
        return Customer.objects.get(pk=self.kwargs['pk']).user

    def get_initial(self):
        initial = super().get_initial()
        initial['dob'] = Customer.objects.get(pk=self.kwargs['pk']).dob
        initial['mobile'] = Customer.objects.get(pk=self.kwargs['pk']).mobile
        return initial



def customer_list_view(request):
    customer = Customer.objects.filter(user__groups__name='customer')
    premium = Customer.objects.filter(user__groups__name='premium')
    context = {'customer': customer, 'premium': premium}
    return render(request, 'customercontrol.html', context)


def staff_list_view(request):
    staff = Customer.objects.filter(user__groups__name='staff')
    context = {'staff': staff}
    return render(request, 'staffcontrol.html', context)

class OrderItemListView(ListView):
    template_name = 'orderdetail.html'
    model = OrderItem
    context_object_name = 'order_items'

    def get_queryset(self):
        return OrderItem.objects.filter(order__id=self.kwargs.get('pk'))


class OrderListView(ListView):
    model = Order
    template_name = 'orderscontrol.html'
    context_object_name = 'orders'

class CustomLoginView(LoginView):
    template_name = 'forms.html'

    # def get_success_url(self, **kwargs):
    #     return reverse("chat")


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'forms.html'
    success_url = reverse_lazy('index')


class Controls(TemplateView):
    template_name = 'controls.html'


class UserDeleteView(DeleteView):
    template_name = 'delete_form.html'
    model = Customer
    success_url = reverse_lazy('controls')

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(ContactView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class OrderDeleteView(DeleteView):
    template_name = 'delete_form.html'
    model = Order
    success_url = reverse_lazy('order_list')

class OrderItemDeleteView(DeleteView):
    template_name = 'delete_form.html'
    model = OrderItem
    success_url = reverse_lazy('order_list')
