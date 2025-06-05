from django import forms
from .models import Order


class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()
