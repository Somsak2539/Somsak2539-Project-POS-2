from django import forms
from django_select2 import forms as s2forms
from .models import InvoiceItem, Product1

class ProductSelect2Widget(s2forms.ModelSelect2Widget):
    search_fields = ['name__icontains', 'barcode__icontains']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
        widgets = {
            'product': ProductSelect2Widget,
        }