from django.forms import ModelForm
from .models import BreakingNews, Predictions, InvestmentStrategies


class BreakingNewsForm(ModelForm):

    class Meta:
        model = BreakingNews
        fields = '__all__'
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class InvestmentStrategiesForm(ModelForm):

    class Meta:
        model = InvestmentStrategies
        fields = '__all__'
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PredictionsForm(ModelForm):

    class Meta:
        model = Predictions
        fields = '__all__'
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'