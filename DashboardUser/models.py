from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from productapp.models import Product1,Category
from decimal import Decimal

# Create your models here.

class Circulation(models.Model):
     Pofitprice = models.DecimalField(max_digits=10, decimal_places=2)            # กำไรสินค้าต่อหน่อย
     
     

#---------------------------------------------------------- สำหรับ invoce.หรือเอกสารต่างๆ --------------------------------------



class Customer(models.Model):
    name = models.CharField("ชื่อลูกค้า", max_length=100)
    address = models.TextField("ที่อยู่")
    phone = models.CharField("เบอร์โทร", max_length=20, blank=True, null=True)
    email = models.EmailField("อีเมล", blank=True, null=True)
    tax_id = models.CharField("เลขประจำตัวผู้เสียภาษี", max_length=20, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField("ชื่อผู้ออกบิล", max_length=100)
    address = models.TextField("ที่อยู่ร้านค้า")
    phone = models.CharField("เบอร์โทร", max_length=20)
    email = models.EmailField("อีเมล", blank=True, null=True)
    tax_id = models.CharField("เลขประจำตัวผู้เสียภาษี", max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("ชื่อสินค้า", max_length=100)
    description = models.TextField("รายละเอียด", blank=True)
    price = models.DecimalField("ราคาขาย", max_digits=10, decimal_places=2)
    barcode = models.CharField("บาร์โค้ด", max_length=13, unique=True)
    image = models.ImageField("รูปภาพสินค้า", upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    class DocumentType(models.TextChoices):
        INVOICE = 'invoice', 'ใบแจ้งหนี้'
        TAX_INVOICE = 'tax_invoice', 'ใบกำกับภาษี'
        QUOTATION = 'quotation', 'ใบเสนอราคา'
        PO = 'po', 'ใบสั่งซื้อ (PO)'
        PR = 'pr', 'ใบขอซื้อ (PR)'

    document_type = models.CharField(
        "ประเภทเอกสาร",
        max_length=20,
        choices=DocumentType.choices,
        default=DocumentType.INVOICE
    )

    invoice_number = models.CharField("เลขที่เอกสาร", max_length=30, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="ลูกค้า")
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, verbose_name="ผู้ออกบิล")
    date = models.DateTimeField("วันที่ออกเอกสาร", default=timezone.now)
    due_date = models.DateField("กำหนดชำระ", blank=True, null=True)
    notes = models.TextField("หมายเหตุ", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_stock = models.BooleanField("อัพเดทสต็อก", default=False)
    include_vat = models.BooleanField("รวม VAT", default=False)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.invoice_number}"

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            prefix = self.document_type.upper()
            today = timezone.now().strftime("%Y%m%d")
            count_today = Invoice.objects.filter(
                invoice_number__startswith=f"{prefix}{today}"
            ).count() + 1
            self.invoice_number = f"{prefix}{today}-{count_today:04d}"
        super().save(*args, **kwargs)

    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items.all())

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")

    product = models.ForeignKey(Product1, on_delete=models.SET_NULL, null=True)
  
    unit_price = models.DecimalField("ราคาต่อหน่วย", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("จำนวน")
    discount = models.PositiveIntegerField("ลดราคา %")
    Tax = models.PositiveIntegerField("Tax 7%")

    @property
    def total_price(self):
    # แปลงค่าลดราคาและภาษีให้เป็น Decimal
        discount_percent = Decimal(self.discount) / Decimal(100)
        tax_percent = Decimal(self.Tax) / Decimal(100)

    # คำนวณราคา
        price = self.quantity * self.unit_price
        discount_amount = price * discount_percent
        price_after_discount = price - discount_amount
        tax_amount = price_after_discount * tax_percent
        total = price_after_discount + tax_amount

        return total
#------------------------------------------------------เก็บข้อมูลใบเสร็จสำหรับอันนี้---------------------------------------------------

class Receipt(models.Model):
    receipt_number = models.CharField(max_length=50, unique=True)  # เลขที่ใบเสร็จ
    date = models.DateTimeField(auto_now_add=True)                 # วันที่ออกใบเสร็จ
    cashier = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)  # พนักงานขาย
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # ยอดรวมทั้งหมด
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)      # ส่วนลด
    payment_method = models.CharField(max_length=20)  # วิธีชำระเงิน (เงินสด, บัตรเครดิต ฯลฯ)
    
    def __str__(self):
        return f"Receipt {self.receipt_number}"

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, related_name='items', on_delete=models.CASCADE)  # ใบเสร็จนี้
    product_name = models.CharField(max_length=100)        # ชื่อสินค้า
    quantity = models.IntegerField()                       # จำนวน
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)  # ราคาต่อหน่วย
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)        # ราคารวมของสินค้านี้ (ก่อนส่วนลด)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"
