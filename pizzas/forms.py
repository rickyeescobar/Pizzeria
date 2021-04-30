from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        label = {'text:':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}