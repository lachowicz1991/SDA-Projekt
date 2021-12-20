from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import FaqForm
from .models import Article, Product, FAQ

LOGGER = getLogger()


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
    context_object_name = 'faqy'

    def get_queryset(self):
        return FAQ.objects.all()


class FaqDetailView(DetailView):
    model = FAQ
    template_name = 'faq_detail.html'
    context_object_name = 'faq'


class FaqCreateView(CreateView):
    template_name = 'faq_form.html'
    form_class = FaqForm
    success_url = reverse_lazy('faq')


class FaqUpdateView(UpdateView):
    template_name = 'faq_form.html'
    model = FAQ
    form_class = FaqForm
    success_url = reverse_lazy('faq')

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class FaqDeleteView(DeleteView):
    template_name = 'faq_delete.html'
    model = FAQ
    success_url = reverse_lazy('faq')
# Create your views here.
