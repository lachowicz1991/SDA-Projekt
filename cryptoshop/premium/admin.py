from django.contrib import admin
from .models import Predictions, InvestmentStrategies, BreakingNews
# Register your models here.

admin.site.register(BreakingNews)
admin.site.register(Predictions)
admin.site.register(InvestmentStrategies)