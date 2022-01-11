
from django.views.generic import ListView, TemplateView
from cart.models import Product
from viewer.models import Article, Advert


# Create your views here.


class CryptoView(TemplateView):
    template_name = "cryptomarket.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CryptoView, self).get_context_data(**kwargs)
        # context['aricels'] = Article.objects.all()
        # context2 = super(PremiumView, self).get_context_data(**kwargs)
        context['adverts'] = Advert.objects.all()
        return context

class TechnicalAnalysis(TemplateView):
    template_name = 'analyst_tech.html'
