from django.contrib.auth.models import User
from django.db.models import Model, TextField, CASCADE, OneToOneField, CharField, URLField, FloatField, EmailField, DateField, ForeignKey
# Create your models here.


class Customer(Model):
	user = OneToOneField(User, on_delete=CASCADE)
	mobile = CharField(max_length=12,null=True)
	dob = DateField(null=True)

	def __str__(self):
		return self.user.username

class Staff(User):
	mobile = CharField(max_length=12)
	dob = DateField()
	rank = CharField(max_length=20)