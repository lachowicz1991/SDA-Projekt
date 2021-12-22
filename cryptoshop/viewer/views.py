from django.shortcuts import render
import requests
from django.views.generic import TemplateView, ListView
from .models import Article

API_KEY = 'ff230ce135704fccb7a61b36132c35f9'


class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'index'


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        print(articles)

    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        print(articles)

    context = {
        'articles' :articles
    }

    return render(request, 'news.html', context)

# Create your views here.
