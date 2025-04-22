from django.db import models
from django.contrib.auth.models import User
from productapp.models import Product1

# Create your models here.
  #จะเป็นส่วนที่สร้างตารางเพื่อที่จะมีการเชื่อมโยงกับ admin
class Cart(models.Model):  
    cart_id=models.CharField(max_length=255,blank=True)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
class CartItem(models.Model):
    product=models.ForeignKey(Product1,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    
    
  
    def sub_total(self):
      return self.product.price*self.quantity
    def __str__ (self):
      return self.product.name +":" +str(self.quantity) # การแปลงข้อมูลเพื่อที่จะไปแสดง ที่เรียกข้อมูลไป debug
    
    