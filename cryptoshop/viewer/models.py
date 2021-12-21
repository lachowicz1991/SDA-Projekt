from django.db.models import Model, TextField, CharField, ForeignKey, IntegerField, DateTimeField, FloatField, ImageField, BooleanField, SET_NULL

# Create your models here.


#  Model used for the articles with external URLs for images.
class Article(Model):
	title = CharField(max_length=128)
	content = TextField()
	image = ImageField(upload_to='articles', blank=True, null=True)


class Adverts(Model):
	title = CharField(max_length=128)
	image = ImageField(upload_to='images/', blank=True, null=True)








