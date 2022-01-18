from django.db.models import Model, CharField, TextField, ImageField, SlugField
from django.utils.text import slugify


# Create your models here.

#Model Prediction(Premium)
class Predictions(Model):
    title = CharField(max_length=128)
    content = TextField()
    short_description = TextField(null=True, blank=True)
    image = ImageField(upload_to='predictions', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url_safe(self):
        try:
            url = self.image.url

        except:
            url = ''
        return url


#Model Investment Strategies(Premium)
class InvestmentStrategies(Model):
    title = CharField(max_length=128)
    content = TextField()
    short_description = TextField(null=True, blank=True)
    image = ImageField(upload_to='images', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url_safe(self):
        try:
            url = self.image.url

        except:
            url = ''
        return url


#Model Breaking News(Premium)
class BreakingNews(Model):
    title = CharField(max_length=128)
    content = TextField()
    short_description = TextField(null=True, blank=True)
    image = ImageField(upload_to='images', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url_safe(self):
        try:
            url = self.image.url

        except:
            url = ''
        return url