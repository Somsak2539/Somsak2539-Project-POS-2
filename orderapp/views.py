from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from cartapp.models import Cart,CartItem #การimport models เข้ามาทำงาน
from orderapp.models import Order,OrderDetail
from productapp.models import Product1
from cartapp.views import create_cartId   #การimport views เข้ามาทำงาน

# Create your views here.
@login_required(login_url="/login")
def orderHistory(request):
    
    
    orders=Order.objects.filter(customer=request.user)  # เรียกใช้ผ่าน modele เมื่อจะให้ไปแสดงที่หน้าจอ order ตัวนี่เพื่อทำการนลูปหน้าจ้าเวลาจะใส่ค่าให้ Html
    return render(request,"orderHistory.html",{"orders":orders})


@login_required(login_url="/login")
def orderDetil(request,order_id):
    order=Order.objects.get(pk=order_id)
    
    if order.customer==request.user:
       order_item= OrderDetail.objects.filter(order=order)
       return render(request,"orderDetail.html",{"order":order,"order_item":order_item})
    else:
        return redirect("/orderHistory")#กำหนดสินในการเข้าถึง ถ้าไม่ได้ทำการlogin ก็จะทำการ redirectไปที่ orderHistory
    



@login_required(login_url="/login")
def order(request):
    
    if request.method=="POST":
        fullname=  request.POST["fullname"]
        phone=request.POST["phone"]
        address= request.POST["address"]
        cart=Cart.objects.get(cart_id=create_cartId(request),customer=request.user) # คือดึงค่าตัวแปรมาจาก cart 
        cartItem=CartItem.objects.filter(cart=cart)  # ดึงค่ามาจาก cartitem
        total=0
        for item in cartItem:
            total+=(item.product.price*item.quantity)
            
            #สร้างใบสร้างซื้อสินค้า
        order=Order.objects.create(
            fullname=fullname,
            phone=phone,
            address=address,
            total=total,
            customer=request.user
            
        )
        order.save()
        #บันทึกรายการสั่งซื้อและตัด Stock  ตัวนี้อยู่ใน OrderDetail 
        for item in cartItem:
           order_detail=OrderDetail.objects.create(
                product=item.product.name,    #ตัวนี้คือproductที่เก็บไว้ในตัวแปรnameมาจากยอดผู้ที่ทำการสั่งซื้อ
                quantity=item.quantity,
                price=item.product.price,
                order=order                          #order เท่ากับ order 
            )
           order_detail.save()
           #ตัด Stock
           product=Product1.objects.get(pk=item.product.id)
           product.stock=(item.product.stock-order_detail.quantity)
           product.save()
           item.delete()

        cart.delete()
        return render(request,"ordercomplete.html")   
    else:
        return render(request,"order.html")
    
    
    