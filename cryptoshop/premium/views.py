from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class CryptoView(TemplateView):
    template_name = "cryptomarket.html"

class TechnicalAnalysis(TemplateView):
    template_name = 'analyst_tech.html'
