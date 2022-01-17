from django.utils.text import slugify
from django.db.models import Model, TextField, CharField,SlugField, ImageField
# Create your models here.


#  Model used for the articles with external URLs for images.

class Article(Model):
    title = CharField(max_length=128)
    content = TextField()
    image = ImageField(upload_to='images', blank=True, null=True)
    slug = SlugField(max_length=128, unique=True)

    def save(self, args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, **kwargs)

    def str(self):
        return self.title

    @property
    def image_url_safe(self):
        try:
            url = self.image.url

        except:
            url = ''
        return url


# Model Adverts similar to article (Home)

class Advert(Model):
	title = CharField(max_length=128)
	content = TextField()
	image = ImageField(upload_to='images', blank=True, null=True)
	slug = SlugField(max_length=128, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	@property
	def image_url_safe(self):
		try:
			url = self.image.url

		except:
			url = ''
		return url



class FAQ(Model):
	question = CharField(max_length=128)
	answer = TextField()
	slug = SlugField(max_length=128, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.question)
		super().save(*args, **kwargs)


