

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
from .models import Receipt, ReceiptItem












@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','tax_id')
    search_fields = ('name', 'phone', 'email','tax_id')


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



#-------------------------------สำหรับการเก็บข้อมูล ReciptItem-------------------------------------------------------


class ReceiptItemInline(admin.TabularInline):  # หรือใช้ StackedInline ก็ได้
    model = ReceiptItem
    extra = 1  # จำนวนฟอร์มเปล่า ๆ ที่โชว์เพิ่มเวลาเพิ่มสินค้าในใบเสร็จ

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'date', 'cashier', 'total_amount', 'payment_method')
    search_fields = ('receipt_number', 'cashier__username')
    list_filter = ('payment_method', 'date')
    inlines = [ReceiptItemInline]  # ให้แสดง ReceiptItem เป็นตารางในหน้า Receipt

@admin.register(ReceiptItem)
class ReceiptItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'receipt', 'quantity', 'price_per_unit', 'subtotal')
    search_fields = ('product_name',)
    list_filter = ('receipt__date',)
    
    
