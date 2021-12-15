from django.db.models import Model, TextField, CharField, FloatField, ImageField

# Create your models here.


#  Model used for the articles with external URLs for images.
class Article(Model):
	title = CharField(max_length=128)
	content = TextField()
	image = ImageField(upload_to='articles', blank=True)


class Product(Model):
	PREMIUM_CHOICE = (('Yes', 'Yes'), ('No', 'No'))

	title = CharField()
	content = TextField()
	premium = TextField(max_length=100, choices=PREMIUM_CHOICE)
	price = FloatField(null=True)
	image = ImageField(upload_to='product', blank=True)
