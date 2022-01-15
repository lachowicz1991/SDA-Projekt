from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateField, CharField, Form, ModelMultipleChoiceField
from .models import Customer
from django.db.transaction import atomic
from django import forms



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	mobile = CharField(max_length=30)

class AdminUserUpdateForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'groups']

	mobile = CharField(max_length=30)
	dob = DateField()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	@atomic
	def save(self, commit=True):
		user = super().save(commit)
		mobile = self.cleaned_data['mobile']
		dob = self.cleaned_data['dob']
		customer = Customer.objects.get(user__pk=user.pk)
		customer.mobile = mobile
		customer.dob = dob
		if commit:
			customer.save()
		return user

class CreateCustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['mobile', 'dob']

class UserCustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['mobile', 'dob']





