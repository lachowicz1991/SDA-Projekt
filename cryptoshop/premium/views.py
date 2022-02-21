from logging import getLogger

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from cart.utils import cartData
from .forms import PredictionsForm, BreakingNewsForm, InvestmentStrategiesForm
from .models import InvestmentStrategies, Predictions, BreakingNews

# Create your views here.

LOGGER = getLogger()


class CryptoView(TemplateView):
    template_name = "cryptomarket.html"

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(CryptoView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class TechnicalAnalysisView(TemplateView):
    template_name = "analyst_tech.html"

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(TechnicalAnalysisView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class PredictionsView( ListView):
    template_name = "predictions.html"
    model = Predictions
    context_object_name = 'predictions'

    def get_queryset(self):
        return Predictions.objects.all()

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(PredictionsView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(TechnicalAnalysisView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class PredictionsDetailView(DetailView):
    model = Predictions
    template_name = 'predictions_detail.html'
    context_object_name = 'prediction'

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(PredictionsDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class PredictionsCreateView(CreateView):
    template_name = 'predictions_form.html'
    form_class = PredictionsForm
    success_url = reverse_lazy('prediction')

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(PredictionsDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class PredictionsUpdateView(UpdateView):
    template_name = 'predictions_form.html'
    model = Predictions
    form_class = PredictionsForm
    success_url = reverse_lazy('prediction')

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(PredictionsView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class PredictionsDeleteView(DeleteView):
    template_name = "predictions_delete.html"
    model = Predictions
    success_url = reverse_lazy('prediction')


class BreakingNewsView(ListView):
    template_name = "breaking_news.html"
    model = BreakingNews
    context_object_name = 'breakings_news'

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(BreakingNewsDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

    def get_queryset(self):
        return BreakingNews.objects.all()

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(BreakingNewsView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context


class BreakingNewsDetailView(DetailView):
    model = BreakingNews
    template_name = 'breaking_news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(BreakingNewsDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context


class BreakingNewsCreateView(CreateView):
    template_name = 'breaking_news_form.html'
    form_class = BreakingNewsForm
    success_url = reverse_lazy('breaking_news')


class BreakingNewsUpdateView(UpdateView):
    template_name = 'breaking_news_form.html'
    model = BreakingNews
    form_class = BreakingNewsForm
    success_url = reverse_lazy('breaking_news')


    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(InvestmentStrategiesDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context

class BreakingNewsDeleteView(DeleteView):
    template_name = "breaking_news_delete.html"
    model = BreakingNews
    success_url = reverse_lazy('breaking_news')


class InvestmentStrategiesView(ListView):
    template_name = "investment_strategies.html"
    model = InvestmentStrategies
    context_object_name = 'strategies'

    def get_queryset(self):
        return InvestmentStrategies.objects.all()

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(InvestmentStrategiesView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context


class InvestmentStrategiesDetailView(DetailView):
    model = InvestmentStrategies
    template_name = "investment_strategies_detail.html"
    context_object_name = 'strategy'

    def get_context_data(self, **kwargs):
        data = cartData(self.request)
        context = super(InvestmentStrategiesDetailView, self).get_context_data(**kwargs)
        context['cartitems'] = data['cartitems']
        return context


class InvestmentStrategiesCreateView( CreateView):
    template_name = "investment_strategies_form.html"
    form_class = InvestmentStrategiesForm
    success_url = reverse_lazy('investment_strategies')


class InvestmentStrategiesUpdateView(UpdateView):
    template_name = "investment_strategies_form.html"
    model = InvestmentStrategies
    form_class = InvestmentStrategiesForm
    success_url = reverse_lazy('investment_strategies')

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class InvestmentStrategiesDeleteView(DeleteView):
    template_name = "investment_strategies_delete.html"
    model = InvestmentStrategies
    success_url = reverse_lazy('investment_strategies')
