from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from accounts.models import Customer
# Create your views here.

def store(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartitems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
		cartitems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartitems': cartitems}
	return render(request, 'store.html', context)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartitems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
		cartitems = order['get_cart_items']
	context = {'items': items, 'order':order, 'cartitems':cartitems}
	return render(request, 'cart.html', context,)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartitems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
		cartitems = order['get_cart_items']
	context = {'items': items, 'order': order, 'cartitems':cartitems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productid = data['productId']
	action = data['action']

	print('Action:',action)
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

