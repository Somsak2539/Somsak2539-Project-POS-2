from django import forms
from django_select2 import forms as s2forms
from .models import InvoiceItem, Product1
from .models import Seller, Customer, Invoice, InvoiceItem


class ProductSelect2Widget(s2forms.ModelSelect2Widget):
    search_fields = ['name__icontains', 'barcode__icontains']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = [
            'product',
            'quantity',
            'unit_price',
            'discount',
            'Tax'
        ]
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
            'unit_price': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'discount': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'Tax': forms.NumberInput(attrs={'value': 7, 'readonly': True}),
        }

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'address', 'phone', 'tax_id', 'email']
        labels = {
            'name': 'ชื่อลูกค้า',
            'address': 'ที่อยู่บริษัท',
            'phone': 'เบอร์โทร',
            'tax_id': 'เลขที่ผู้เสียภาษี',
            'email': 'อีเมล',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Client name'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'rows': 3,
                'placeholder': 'ที่อยู่บริษัท'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': '0843285745'
            }),
            'tax_id': forms.NumberInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': '00545485465'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'somsaksonngai@gmail.com'
            }),
        }  

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'document_type',
            'customer',
            'seller',
            'date',
            'due_date',
            'notes',
            'update_stock',
            'include_vat'
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone', 'email', 'tax_id']  # เพิ่ม tax_id เข้าไป
        labels = {
            'name': 'ชื่อลูกค้า',
            'address': 'ที่อยู่',
            'phone': 'เบอร์โทร',
            'email': 'อีเมล',
            'tax_id': 'เลขที่ผู้เสียภาษี',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'ชื่อลูกค้า'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'rows': 3,
                'placeholder': 'ที่อยู่'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'เบอร์โทร'
            }),
            'tax_id': forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'เลขที่ผู้เสียภาษี'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'example@email.com'
            }),
        }

InvoiceItemFormSet = forms.inlineformset_factory(
    Invoice,
    InvoiceItem,
    form=InvoiceItemForm,
    extra=1,
    can_delete=True
)

