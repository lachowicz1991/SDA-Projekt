from logging import getLogger

import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from cart.utils import cartData
from .forms import FaqForm, AdvertForm, ArticleForm
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
        url = f'https://newsapi.org/v2/top-headlines?country=pl&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        print(articles)
    data = cartData(request)
    cartitems = data['cartitems']

    context = {
        'articles': articles,
        'cartitems': cartitems,
    }

    return render(request, 'news.html', context)


# View for the FAQ / Tomek
class FaqControlView(ListView):
    template_name = 'faq-control.html'
    model = FAQ
    context_object_name = 'faqy'


class FaqView(ListView):
    template_name = 'faq.html'
    model = FAQ
    context_object_name = 'faqy'

    def get_queryset(self):
        return FAQ.objects.all()

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(FaqView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        context['adverts'] = Advert.objects.all()
        return context


class FaqDetailView(DetailView):
    model = FAQ
    template_name = 'faq_detail.html'
    context_object_name = 'faq'


class FaqCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'faq_form.html'
    form_class = FaqForm
    success_url = reverse_lazy('faq-control')
    permission_required = 'viewer.add_faq'


class FaqUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'faq_form.html'
    model = FAQ
    form_class = FaqForm
    success_url = reverse_lazy('faq-control')
    permission_required = 'viewer.change_faq'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class FaqDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'faq_delete.html'
    model = FAQ
    success_url = reverse_lazy('faq-control')
    permission_required = 'viewer.delete_faq'

# # View for Home / Emil


class AdvertControlView(ListView):
    template_name = 'advert-control.html'
    model = Advert
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.all()

class AdvertView(ListView):
    template_name = 'advert.html'
    model = Advert
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.all()

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(AdvertView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        context['articles'] = Article.objects.all()
        return context


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'advert_detail.html'
    context_object_name = 'advert'


class AdvertCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'advert_form.html'
    form_class = AdvertForm
    success_url = reverse_lazy('advert-control')
    permission_required = 'viewer.add_advert'



class AdvertUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'advert_form.html'
    model = Advert
    form_class = AdvertForm
    success_url = reverse_lazy('advert-control')
    permission_required = 'viewer.change_advert'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class AdvertDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'advert_delete.html'
    model = Advert
    success_url = reverse_lazy('advert-control')
    permission_required = 'viewer.delete_advert'


# View for Home / Emil (Article)
class ArticleControlView(ListView):
    template_name = 'article-control.html'
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()


class ArticleView(ListView):
    template_name = 'article.html'
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article-control')
 #   permission_required = 'viewer.add_article'


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'article_form.html'
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('article-control')
    permission_required = 'viewer.change_article'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('article-control')
    permission_required = 'viewer.delete_article'