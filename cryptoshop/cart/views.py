from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product, Order
# Create your views here.

# View for the courses and cart / Matt


class CoursesView(ListView):
    template_name = 'courses.html'
    model = Product
    context_object_name = 'products'

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()

	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
	context = {'items': items, 'order':order}
	return render(request, 'cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
	context = {'items': items, 'order': order}
	return render(request, 'checkout.html', context)