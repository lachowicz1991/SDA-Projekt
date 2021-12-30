from django.db.models import Model, TextField, CharField, ImageField
from django.db.models import SlugField
from django.utils.text import slugify


# Create your models here.


#  Model used for the articles with external URLs for images.
class Article(Model):
    title = CharField(max_length=128)
    content = TextField()
    image = ImageField(upload_to='articles', blank=True, null=True)


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


class FAQ(Model):
    question = CharField(max_length=128)
    answer = TextField()
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        super().save(*args, **kwargs)
