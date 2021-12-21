from django.db.models import Model, TextField, CharField, FloatField, ImageField, SlugField
from django.utils.text import slugify

#  Model used for the articles with external URLs for images.
class Article(Model):
	title = CharField(max_length=128)
	content = TextField()
	image = ImageField(upload_to='articles', blank=True)

# Model Adverts similar to article (Home)
class Advert(Model):
	title = CharField(max_length=128)
	content = TextField()
	image = ImageField(upload_to='adverts', blank=True)
	slug = SlugField(max_length=128, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

#	def __str__(self):
#		return self.title


class Product(Model):
	PREMIUM_CHOICE = (('Yes', 'Yes'), ('No', 'No'))

	title = CharField(max_length=100)
	short_description = TextField()
	content = TextField()
	premium = CharField(max_length=100, choices=PREMIUM_CHOICE)
	price = FloatField(null=True)
	image = ImageField(upload_to='product', blank=True)


class FAQ(Model):
	question = CharField(max_length=128)
	answer = TextField()
	slug = SlugField(max_length=128, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.question)
		super().save(*args, **kwargs)


