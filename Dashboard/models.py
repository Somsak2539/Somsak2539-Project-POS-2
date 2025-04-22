from django.db import models
from django.contrib.auth.models import User


class OrderSele(models.Model):
     product = models.CharField(max_length=255)                                   # รายการสินค้าที่ขายได้
     price = models.DecimalField(max_digits=10, decimal_places=2)                 # ราคาสินค้า
     quantity = models.IntegerField()                                             # จำนวณสินค้าที่ขายได้
     created = models.DateTimeField(auto_now=True)                                # วันที่ขายสินค้า 
     customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)   # Userผู้ทำการเฝ้าเครื่อง
     Pofitprice = models.DecimalField(max_digits=10, decimal_places=2)            # กำไรสินค้าต่อหน่อย
# Create your models here.


class SaleRecord(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    entered_amount = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()
    Pofitprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)       
    stock_adjustments = models.JSONField()  # ใช้ JSONField สำหรับบันทึกข้อมูล Array
    cashier = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    
    
    
    
    
    
    class Meta:
        verbose_name = "รายการสินค้าที่บันทึก"  # เปลี่ยนชื่อที่แสดงใน Admin
        verbose_name_plural = "บันทึกรายการสำหรับการขาย"  # ชื่อพหูพจน์ใน Admin

    
    def get_stock_adjustment_by_index(self, index):
        """ดึงรายการ stock_adjustments ตามตำแหน่ง index"""
        try:
            return self.stock_adjustments[index]
        except (IndexError, TypeError):
            return None  # กรณีไม่มีรายการหรือ index เกิน