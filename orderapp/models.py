                
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    fullname = models.CharField(max_length=255, blank=True)  # ชื่อผู้สั่งซื้อ
    phone = models.CharField(max_length=50, blank=True)      # เบอร์โทร
    address = models.CharField(max_length=255, blank=True)   # ที่อยู่
    total = models.DecimalField(max_digits=10, decimal_places=2)  # ยอดรวม
    created = models.DateTimeField(auto_now_add=True)        # วันที่สร้างคำสั่งซื้อ
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # ผู้สั่งซื้อ

    def __str__(self):
        return f"Order {self.id} - {self.fullname}"
    
    def total_with_comma(self):
        # เพิ่ม comma ใน total
        return f"{self.total:,.2f}"
    total_with_comma.short_description = "Total (formatted)"  # เปลี่ยนชื่อใน admin view
    
    
    
class OrderDetail(models.Model):
    

    product = models.CharField(max_length=255)               # ชื่อสินค้า
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ราคาสินค้า
    quantity = models.IntegerField()                         # จำนวนสินค้า
    created = models.DateTimeField(auto_now=True)            # วันที่เพิ่มสินค้าในคำสั่งซื้อ
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # ความสัมพันธ์กับ Order


    def sub_total(self):
        
        return f"{self.price*self.quantity:,.2f}" #ทำหารแปลงให้เป็น commaขั้นเพือที่จะดูได้ง่ายขึ้น 
    def __str__(self):
        return f"{self.product} - {self.order.fullname}"  # ตัวอย่าง: หาก Order มี id=1 และ fullname="John Doe" การแสดงผลจะเป็น: Order 1 - John Doe
    
    
    def price_with_comma(self):
        # เพิ่ม comma ใน price
        return f"{self.price:,.2f}"
    price_with_comma.short_description = "price (formatted)"  # เปลี่ยนชื่อใน admin view

    
    def DetailBuy(self):
        # ดึงข้อมูลรายละเอียดผู้ซื้อจากคำสั่งซื้อ (Order)
        return f"Customer: {self.order.customer.username}, Address: {self.order.address}, Phone: {self.order.phone}"
    DetailBuy.short_description = "Customer Details"  # เปลี่ยนชื่อใน admin view