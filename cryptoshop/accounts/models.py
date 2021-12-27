from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, TextField, CASCADE, OneToOneField, CharField, URLField, FloatField, EmailField, DateField, ForeignKey
# Create your models here.


class Customer(Model):
	user = OneToOneField(User, on_delete=CASCADE)
	LEVEL = (('Free', 'Free'),('Premium', 'Premium'))
	mobile = CharField(max_length=12)
	dob = DateField()
	subscription = CharField(max_length=20, choices=LEVEL)


	def __str__(self):
		return self.user

class Staff(User):
	mobile = CharField(max_length=12)
	dob = DateField()
	rank = CharField(max_length=20)
