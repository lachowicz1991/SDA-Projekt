from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, TextField, CharField, URLField, FloatField, EmailField, DateField, ForeignKey
# Create your models here.

class Customer(User):
	LEVEL = (('Free', 'Free'),('Premium', 'Premium'))

	mobile = CharField(max_length=12)
	email = EmailField()
	dob = DateField()
	basket = ForeignKey
	subscription = CharField(max_length=20, choices=LEVEL)

class Staff(Customer):
	rank = CharField(max_length=20)
