from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Article

class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'index'


# Create your views here.
