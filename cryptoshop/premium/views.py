from logging import getLogger

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PredictionsForm, BreakingNewsForm, InvestmentStrategiesForm
from .models import InvestmentStrategies, Predictions, BreakingNews

# Create your views here.

LOGGER = getLogger()


def is_premium(user):
    return user.groups.filter(name='Premium').exists()


class PremiumView(TemplateView):
    template_name = "premium.html"


class CryptoView(PermissionRequiredMixin, TemplateView):
    template_name = "cryptomarket.html"
    permission_required = 'premium.view_predictions'


class TechnicalAnalysisView(PermissionRequiredMixin, TemplateView):
    template_name = "analyst_tech.html"
    permission_required = 'premium.view_predictions'


class PredictionsView(PermissionRequiredMixin, ListView):
    template_name = "predictions.html"
    model = Predictions
    context_object_name = 'predictions'
    permission_required = 'premium.view_predictions'

    def get_queryset(self):
        return Predictions.objects.all()


class PredictionsDetailView(PermissionRequiredMixin, DetailView):
    model = Predictions
    template_name = 'predictions_detail.html'
    context_object_name = 'prediction'
    permission_required = 'premium.view_predictions'


class PredictionsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'predictions_form.html'
    form_class = PredictionsForm
    success_url = reverse_lazy('prediction')
    permission_required = 'premium.add_predictions'


class PredictionsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'predictions_form.html'
    model = Predictions
    form_class = PredictionsForm
    success_url = reverse_lazy('prediction')
    permission_required = 'premium.change_predictions'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class PredictionsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "predictions_delete.html"
    model = Predictions
    success_url = reverse_lazy('prediction')
    permission_required = 'premium.delete_predictions'


class BreakingNewsView(PermissionRequiredMixin, ListView):
    template_name = "breaking_news.html"
    model = BreakingNews
    context_object_name = 'breakings_news'
    permission_required = 'premium.view_breaking_news'

    def get_queryset(self):
        return BreakingNews.objects.all()


class BreakingNewsDetailView(PermissionRequiredMixin, DetailView):
    model = BreakingNews
    template_name = 'breaking_news_detail.html'
    context_object_name = 'news'
    permission_required = 'premium.view_breaking_news'


class BreakingNewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'breaking_news_form.html'
    form_class = BreakingNewsForm
    success_url = reverse_lazy('breaking_news')
    permission_required = 'premium.add_breaking_news'


class BreakingNewsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'breaking_news_form.html'
    model = BreakingNews
    form_class = BreakingNewsForm
    success_url = reverse_lazy('breaking_news')
    permission_required = 'premium.change_breaking_news'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class BreakingNewsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "breaking_news_delete.html"
    model = BreakingNews
    success_url = reverse_lazy('breaking_news')
    permission_required = 'premium.delete_breaking_news'


class InvestmentStrategiesView(PermissionRequiredMixin, ListView):
    template_name = "investment_strategies.html"
    model = InvestmentStrategies
    context_object_name = 'strategies'
    permission_required = 'premium.view_investment_strategies'

    def get_queryset(self):
        return InvestmentStrategies.objects.all()


class InvestmentStrategiesDetailView(PermissionRequiredMixin, DetailView):
    model = InvestmentStrategies
    template_name = "investment_strategies_detail.html"
    context_object_name = 'strategy'
    permission_required = 'premium.view_investment_strategies'


class InvestmentStrategiesCreateView(PermissionRequiredMixin, CreateView):
    template_name = "investment_strategies_form.html"
    form_class = InvestmentStrategiesForm
    success_url = reverse_lazy('investment_strategies')
    permission_required = 'premium.add_investment_strategies'


class InvestmentStrategiesUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "investment_strategies_form.html"
    model = InvestmentStrategies
    form_class = InvestmentStrategiesForm
    success_url = reverse_lazy('investment_strategies')
    permission_required = 'premium.change_investment_strategies'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class InvestmentStrategiesDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "investment_strategies_delete.html"
    model = InvestmentStrategies
    success_url = reverse_lazy('investment_strategies')
    permission_required = 'premium.delete_investment_strategies'
