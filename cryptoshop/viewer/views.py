from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Article, Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'article'

# View for the courses / Matt
class CoursesView(ListView):
    template_name = 'courses.html'
    model = Product
    context_object_name = 'product'


# Create your views here.
