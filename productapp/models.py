


from django.db import models
from django.apps import AppConfig


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_trending = models.BooleanField(default=False)
    image = models.ImageField(upload_to="product", blank=True)
    
    


# โมเดล Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ชื่อหมวดหมู่

    def __str__(self):
        return self.name
    
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "ประเภทรายการสินค้า"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    

# โมเดล Product
class Product1(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,verbose_name="หมวดหมู่สินค้า")  
    name = models.CharField("ชื่อสินค้า", max_length=100)
    description = models.TextField("รายละเอียดสินค้า", max_length=500)
    price = models.DecimalField("ราคาขาย", max_digits=10, decimal_places=2)
    stock = models.DecimalField("จำนวนในสต๊อก", max_digits=10, decimal_places=2)
    is_trending = models.BooleanField("สินค้าแนะนำ", default=False)
    image = models.ImageField("รูปสินค้า", upload_to="product")
    profitprice = models.DecimalField("ราคากำไร", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("วันที่เพิ่มสินค้า", auto_now_add=True)
    updated_at = models.DateTimeField("วันที่แก้ไขล่าสุด", auto_now=True)
    barcode = models.CharField("บาร์โค้ด", max_length=13, unique=True)

    def __str__(self):
        return self.name
    
    
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "รายการสินค้า"
    
    
    def __str__(self):
        return self.name


class frolink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    
    
    class Meta:
        verbose_name = "frolink"
        verbose_name_plural = "กลับไปหน้า DashBord"
    

    def __str__(self):
        return self.name
    
    


    
    
