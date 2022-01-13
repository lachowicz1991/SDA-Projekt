from django.db.models import Model, CharField, TextField, ImageField, SlugField
from django.utils.text import slugify


# Create your models here.
#Model Prediction(Premium)
class Predictions(Model):
    title = CharField(max_length=128)
    content = TextField()
    short_description = TextField()
    image = ImageField(upload_to='predictions', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        super().save(*args, **kwargs)


#Model Investment Strategies(Premium)
class InvestmentStrategies(Model):
    title = CharField(max_length=128)
    content = TextField()
    short_description = TextField()
    image = ImageField(upload_to='images', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        super().save(*args, **kwargs)


#Model Breaking News(Premium)
class BreakingNews(Model):
    title = CharField(max_length=128)
    content = TextField()
    short_description = TextField()
    image = ImageField(upload_to='images', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        super().save(*args, **kwargs)