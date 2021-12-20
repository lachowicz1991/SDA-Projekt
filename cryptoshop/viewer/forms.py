from django.forms import ModelForm
from .models import FAQ


class FaqForm(ModelForm):

    class Meta:
        model = FAQ
        fields = '__all__'
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'