from django.db import models
from django.db.models import Model, TextField, CharField, ForeignKey, IntegerField, DateTimeField, FloatField, ImageField, BooleanField, SET_NULL
from accounts.models import Customer
# Create your models here.


class Product(Model):
	PREMIUM_CHOICE = (('Yes', 'Yes'), ('No', 'No'))

	name = CharField(max_length=200)
	short_description = TextField(null=True, blank=True)
	price = FloatField()
	digital = BooleanField(default=False, null=True, blank=False)
	image = ImageField(null=True, blank=True, upload_to="images/")
	premium = CharField(max_length=100, choices=PREMIUM_CHOICE)

	def __str__(self):
		return self.name

	@property
	def image_url_safe(self):
		try:
			url = self.image.url

		except:
			url = ''
		return url


class Order(Model):
	customer = ForeignKey(Customer, on_delete=SET_NULL, null=True, blank=True)
	date_ordered = DateTimeField(auto_now_add=True)
	complete = BooleanField(default=False, null=True, blank=False)
	transaction_id = CharField(max_length=100, null=True)

	def __str__(self):
			return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total


class OrderItem(Model):
	product = ForeignKey(Product, on_delete=SET_NULL, null=True)
	order = ForeignKey(Order, on_delete=SET_NULL, null=True)
	quantity = IntegerField(default=0, null=True, blank=True)
	date_added = DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class ShippingAddress(Model):
	customer = ForeignKey(Customer, on_delete=SET_NULL, null=True)
	order = ForeignKey(Order, on_delete=SET_NULL, null=True)
	address = CharField(max_length=200, null=False)
	city = CharField(max_length=200, null=False)
	state = CharField(max_length=200, null=False)
	date_added = DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address