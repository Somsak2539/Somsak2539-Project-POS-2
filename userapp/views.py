from django.shortcuts import render,redirect #
from django.contrib import messages          #import messages ออกมาเพื่อแสดงการเตือน
from django.contrib.auth.models import  User,auth # การ import User เข้ามาทำงานในนี้ 



# Create your views here.

def  register(request):
    
    if request.method=="POST": #  เป็นการรับค่าจากปุ่มด้านที่ผู้ใช้กรอกเข้ามา สามารถดูmethodได้ .
        
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        if username=='' or email=='' or password=='':
            messages.warning(request,"กรุณป้อนข้อมูลให้ครบ")  # ทำเป็น tags ก็ได้เผื่อทำการเรียกใช้ อย่างเช่น  warning 
            return redirect("/register")
        
        
        else:    # เมื่อทำทุกอย่างถูกต้องก็จะเข้ามาเคือข่ายนี้ 
            
            if User.objects.filter(username=username).exists(): # เป็นการกรองข้อมูลว่ามีคนใช้ Username นี้ไหมถ้ามีคนใช้ก็จะแสดงว่า Userนี้มีคนใช้งานแล้ว .
                messages.warning(request,"Username นี้มีคนใช้งานแล้ว")
                return redirect("/register")
            else:
                user=User.objects.create_user( 
                    username=username,   
                    email=email,
                    password=password   
                )
                user.save()
                messages.success(request,"สร้างบัญชีผู้ใช่เรียบร้อย")   # ทำเป็น tags ก็ได้เผื่อทำการเรียกใช้ อย่างเช่น  success  .
                return redirect("/login")
        
    else :
         return render(request,"register.html")
     
     

def login(request):
  
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if username=="" or password=='':
            messages.warning(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/login")
        
        else:
            user=auth.authenticate(username=username,password=password)   #ทำการเปรียบเทียบว่ามีข้อมูลตรงกับฐานข้อมูลแล้วหรือไม่
            if user is not None:        # ทำการตรวจสอบว่ามีข้อมูลในฐานข้อมูลหรือไม่ 
                auth.login(request,user)
                return redirect("/")  #ถ้าเครื่องหมายถูกต้องก็จะทำการเข้ามาหน้าตรงนี้  ลองตามไปที่ในส่วนของ ตัว Layout น่ะว่ามีการตั้งค่าจังไงการจัดระดับการเข้าถึงสำหรับโปรแกรม
            else:
                messages.warning(request,"ไม่พบบัญชีข้อมูลในระบบ")
                return redirect("/login")
    else:
        return render(request,"login.html")
 
 
 
 
def logout(request):
    auth.logout(request)
    return redirect("/login")
   
