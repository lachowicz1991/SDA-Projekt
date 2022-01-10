from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateField, CharField
from .models import Customer
from django import forms



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	mobile = CharField(max_length=30)

class CreateCustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['mobile', 'dob']



