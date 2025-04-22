
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from productapp.models import Product1
from cartapp.models import Cart,CartItem

# Create your views here.
#เก็บข้อมูลตะกล้าสินค้าลงในข้อมูล 
def create_cartId(request):
   cart=request.session.session_key
   if not cart:
      cart=request.session.create() #เป็นการเข้าถึงข้อมูลในตระกล้าสินค้า   
   return cart
#----------------------------------------------------------------------------------------
@login_required(login_url="/login") #ในกรณีที่ผู้ใช้ ยังไม่เข้าสู่ระบบก็จะเข้าไปสู่หน้า login ก่อน เป็นฟั่งชั่น django 
def cart(request):
   
   counter=0
   total=0
   try:
      #ดึงข้อมูลตะกร้าสินค้า
      cart=Cart.objects.get(cart_id=create_cartId(request),customer=request.user)
      #ดึงข้อมูลสินค้าในตะกร้า
      cartItem=CartItem.objects.filter(cart=cart)
      for item in cartItem:
         counter+=item.quantity
         total+=(item.product.price*item.quantity)
         
   except (Cart.DoesNotExist,CartItem.DoesNotExist):
      cart=None
      cartItem=None
   #เมื่อทำงานเสร็จก็โยนเข้ามาในนี้ก็จะเอาขอมูลสามส่วนนี้ไปไปในข้อมูลตะกร้าสินค้า
   return render (request,"cart.html",{"cartItem":cartItem,"total":total,"counter":counter})

#----------------------------------------------------------------------------------------


@login_required(login_url="/login")

def addCart(request,product_id):   #การเพิ่มตระกร้า 
   product=Product1.objects.get(pk=product_id)
   
   
   #สร้างตะกร้าสินค้า
   #ในส่วนนี้จะเป็นต้องสร้างตะกร้าสินค้าเมื่อมีการยิบครั้งแรกก็จะเข้าไปในนี้
   
   try:
        cart = Cart.objects.get(cart_id=create_cartId(request))
        
        # ไม่มีตะกร้าสินค้าผู้ใช้จำเป็นต้องสร้าง
   except Cart.DoesNotExist: 
       
        cart = Cart.objects.create(
            cart_id=create_cartId(request),
            customer=request.user
        )
        cart.save()  #บันทึกรายการสินค้าในตะกร้า
     

   try :
    #่ซื้อสินค้าตัวเดิม
      Cart_Item=CartItem.objects.get(product=product,cart=cart)
      
      if Cart_Item.quantity<Cart_Item.product.stock:
         
            Cart_Item.quantity+=1
            Cart_Item.save()
            
                
   except CartItem.DoesNotExist:  
      
   
      CartItem.objects.create(
      product=product,
      cart=cart,
      quantity=1,   

      ) 
      return redirect("/cart") #เพื่มมีการทำการยิบสินค้าให้มันการ returnไปที่ ("/cart ตัวนี้ ")ทุกบันทันมีความจำเป็นหมด
   print(f"Cart: {cart}, Product: {product}")
   print(Cart_Item)

        
          #บันทึกรายการสินค้าใหม่
   return redirect("/cart")        
#------------------------------------------------------------------------------------------------------
@login_required(login_url="/login")
def removeCart(request,product_id):  #ทำการประกาศfucntionขึ้นมา ค่าที่ขอเป็น product id
   
   cart=Cart.objects.get(cart_id=create_cartId(request),customer=request.user)  #เข้าไปเรียกใช้ที่ตัวแปร Cartที่ตัว modle แล้วทำการเรียกใช้ cart ขึ้นมา=การสร้างcreate_cartId
   product=Product1.objects.get(pk=product_id)
   cartItem=CartItem.objects.get(product=product,cart=cart)#สินค้าที่ต้องการจะลบ
   cartItem.delete()
   return redirect("/cart")

