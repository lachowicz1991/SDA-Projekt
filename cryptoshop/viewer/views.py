from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Article, Product, FAQ
from .forms import FaqForm
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'article'


# View for the courses / Matt
class CoursesView(ListView):
    template_name = 'courses.html'
    model = Product
    context_object_name = 'product'

# View for the FAQ / Tomek


class FaqView(ListView):
    template_name = 'faq.html'
    model = FAQ
    context_object_name = 'article'


class FaqCreateView(CreateView):
    template_name = "faq_form.html"
    form_class = FaqForm
    success_url = reverse_lazy('faq')

# Create your views here.
