

# Register your models here.py
from .forms import InvoiceItemForm
from django.apps import AppConfig
from django.contrib import admin
from .models import Customer, Seller, Product, Invoice, InvoiceItem
from productapp.models import Product1,Category
import datetime
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
from rangefilter.filters import DateRangeFilter
from django import forms












@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'tax_id')
    search_fields = ('name', 'phone', 'email', 'tax_id')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'barcode')
    search_fields = ('name', 'barcode')
    list_filter = ('price',)


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'document_type', 'customer', 'seller', 'date', 'total_amount')
    search_fields = ('invoice_number', 'customer__name')
    
    list_filter = ('document_type',('date', DateRangeFilter),)
    inlines = [InvoiceItemInline]
    readonly_fields = ('invoice_number', 'created_at', 'total_amount')


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
  
    list_display = ('invoice', 'product','quantity', 'unit_price', 'total_price')
