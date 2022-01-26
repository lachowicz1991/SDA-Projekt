import datetime
import json
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .utils import cartData
from .forms import ProductForm
from .models import *
from django.contrib.auth.models import Group

# Create your views here.


class CourseDetailView(DetailView):
    model = Product
    template_name = 'course_detail.html'
    context_object_name = 'product_detail'

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

def store(request):
    data = cartData(request)
    cartitems = data['cartitems']

    products = Product.objects.all()
    context = {'products': products, 'cartitems': cartitems}
    return render(request, 'store.html', context)


def cart(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartitems = data['cartitems']

    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'cart.html', context, )


def checkout(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartitems = data['cartitems']

    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productid = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId', productid)

    customer = request.user.customer
    product = Product.objects.get(id=productid)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    print('DATA:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = data['form']['total']
        order.transaction_id = transaction_id
        # # Needs order_id for filter :(
        # premium = OrderItem.objects.filter(order__id=order_id).filter(product__name='premium').exist()
        # # Under construction
        # if premium:
        #     group = Group.objects.get(name='customer')
        #     customer.groups.remove(group)
        #     group = Group.objects.get(name='premium')
        #     customer.groups.add(group)


        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
            )

    else:
        print('User is not logged in...')
    return JsonResponse('Payment complete!', safe=False)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('store')
    permission_required = 'cart.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product_form.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('store')
    permission_required = 'cart.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_form.html'
    model = Product
    success_url = reverse_lazy('store')
    permission_required = 'cart.delete_product'
