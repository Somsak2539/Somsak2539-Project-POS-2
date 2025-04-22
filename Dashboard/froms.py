from django import forms
from .models import Product1

class Product1Form(forms.ModelForm):
    class Meta:
        model = Product1
        fields = '__all__'
        widgets = {
            'barcode': forms.TextInput(attrs={'style': 'width: 400px;'}),  # ขยายช่องให้กว้าง 400px
        }
