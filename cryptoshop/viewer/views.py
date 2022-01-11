from logging import getLogger

import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import FaqForm, AdvertForm
from .models import Article, Advert, FAQ

API_KEY = 'ff230ce135704fccb7a61b36132c35f9'

LOGGER = getLogger()




def news(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        print(articles)

    elif category:

        url = f'https://newsapi.org/v2/top-headlines?category={category}&country=pl&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        print(articles)

    else:
        url = f'https://newsapi.org/v2/top-headlines?country=PL&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        print(articles)

    context = {
        'articles': articles
    }

    return render(request, 'news.html', context)


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


# # View for Home / Emil

class AdvertView(ListView):
    template_name = 'advert.html'
    model = Advert
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.all()


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'advert_detail.html'
    context_object_name = 'advert'


class AdvertCreateView(CreateView):
    template_name = 'advert_form.html'
    form_class = AdvertForm
    success_url = reverse_lazy('index')


class AdvertUpdateView(UpdateView):
    template_name = 'advert_form.html'
    model = Advert
    form_class = AdvertForm
    success_url = reverse_lazy('advert')

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class AdvertDeleteView(DeleteView):
    template_name = 'advert_delete.html'
    model = Advert
    success_url = reverse_lazy('advert')