from django.forms import CharField, DateField, BooleanField, CheckboxInput, Textarea, ImageField, Form, FloatField, IntegerField, ModelChoiceField, ModelForm, Textarea
from django.core.exceptions import ValidationError
from .models import Product
from datetime import date
import re

PREMIUM_CHOICE = (('Yes', 'Yes'), ('No', 'No'))


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

	# PREMIUM_CHOICE = (('Yes', 'Yes'), ('No', 'No'))

	# name = CharField(max_length=200)
	# short_description = CharField(max_length=200, widget=Textarea)
	# price = FloatField()
	# digital = BooleanField(widget=CheckboxInput)
	# image = ImageField()
	# premium = CharField(max_length=100, choices=PREMIUM_CHOICE)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

