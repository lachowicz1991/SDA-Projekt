from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Article, Adverts

class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'index'


class AdvertView(ListView):
    template_name = 'index.html'
    model = Adverts
    context_object_name = 'adverts'

# Create your views here.
