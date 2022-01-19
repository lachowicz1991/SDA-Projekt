from .models import Order

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartitems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
		cartitems = order['get_cart_items']
	return {'cartitems': cartitems, 'order':order, 'items':items}