from rest_framework.response import Response
from django.shortcuts import render
from django.urls import path
from productapp.models import Product1,Category #ทำการดึกข้อมูลจาก folder product ของไฟค์ models แล้วดึงข้อมูล product 1 เข้ามาทำงาน 
from Dashboard.models import SaleRecord
from .models import Circulation
from Dashboard.views import SaveSaleRecordAPIView
from datetime import datetime, timedelta
from django.db.models import Sum  # ✅ นำเข้า Sum
from django.contrib import messages
from django.http import HttpResponse
from django.utils.timezone import now
from django.http import JsonResponse
from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal, InvalidOperation
import pytz
import json  # ✅ ใช้ json.loads() ถ้าข้อมูลเก็บเป็น string
from django.db.models.functions import TruncDate, TruncWeek, TruncMonth  #ตัด timestamp เป็น รายวัน,ตัด timestamp เป็น รายสัปดาห์,ตัด timestamp เป็น รายเดือน
from rest_framework.views import APIView # เรียกเข้า API View
#สำหรับการเข้าสู่ระบบการใช้งาน---------------------------------
from django.shortcuts import render,redirect #
from django.contrib import messages,auth         #import messages ออกมาเพื่อแสดงการเตือน
from django.contrib.auth.models import  User,auth # การ import User เข้ามาทำงานในนี้ 
#------------------------กำหนดสิทธิ์เฉพราะคนที่อยู่ใน groping เท่านั้นที่จะสามารถเข้ากลุ่มได้
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required,user_passes_test
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib import messages,auth
from itertools import groupby
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status  # เรียกเข้า API View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect, reverse



#@user_passes_test(is_special_admin)


def invoiceAdd(request):
    
    return render(request,"app-invoiceAdd.html")



def apps_add_product(request):
    products = Product1.objects.all()
    return render(request, "apps_add_product.html", {"products": products})











# การอนุญาติให้เข้ากลุ่มไม่ว่าจะเป็น group ไดกลุ่มหนึ่ง

def has_permission(user):
    """ ตรวจสอบว่า User อยู่ในกลุ่ม 'group1' หรือ 'SpecialAdmin' """
    in_group1 = user.is_authenticated and user.groups.filter(name='group1').exists()
    in_special_admin = user.is_authenticated and user.groups.filter(name='SpecialAdmin').exists()
    
    # Debugging
    #print(f"🔍 Checking Permissions for {user.username}: Group1={in_group1}, SpecialAdmin={in_special_admin}")

    return in_group1 or in_special_admin  # ✅ ถ้ามีสิทธิ์กลุ่มใดกลุ่มหนึ่งก็ให้ผ่าน


def is_special_admin(user):
    #print(f"Checking access for: {user}")
    #print(f"User Authenticated: {user.is_authenticated}")
    #print(f"User Groups: {user.groups.all()}")
    return user.is_authenticated and user.groups.filter(name='SpecialAdmin').exists()

# ✅ สำหรับการเรียกใช้หน้าเพจ AJax
def apps_ecommerceCartAjax(request):
    
    return render(request, 'apps-ecommerceCartAjax.html')





#------------------------------------------สำหรับการลด stock ----------------------------------------------------

def reduce_stock(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product1, id=product_id)
        quantity = int(request.POST.get('quantity', 1))  # จำนวนที่จะลดจาก stock
        if product.stock >= quantity:
            product.stock -= quantity
            product.save()
            return JsonResponse({'success': True, 'message': f'ลดสต็อกสำเร็จ! สินค้าเหลือ {product.stock}'})
        else:
            return JsonResponse({'success': False, 'message': 'จำนวนสินค้าไม่เพียงพอ'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})




class UpdateStockAPIView(APIView):
    permission_classes = [AllowAny]  # ✅ ปิดการตรวจสอบสิทธิ์ (ใช้ AllowAny แทนได้)

    def put(self, request, *args, **kwargs):
        updates = request.data.get("updates", [])
       
        print("📥 ได้รับข้อมูล:", request.data)


        if not updates:
            return Response({"error": "No updates provided"}, status=status.HTTP_400_BAD_REQUEST)

        response_data = []
        for update in updates:
            try:
                product = Product1.objects.filter(name=update["product"]).first()  # ✅ ใช้ `.filter().first()` ป้องกัน MultipleObjectsReturned
                if not product:
                    return Response({"error": f"Product {update['product']} not found"}, status=status.HTTP_404_NOT_FOUND)

                product.stock -= Decimal(update["quantity"])  # ✅ แปลงเป็น Decimal product.stock=product.stock-quantity  เกิดจากการนำไปลบกัน
                if product.stock < 0:
                    return Response(
                        {"error": f"Not enough stock for product {product.name}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                product.save()
                response_data.append({
                    "product": product.name,
                    "updated_stock": product.stock,
                })

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"updated": response_data}, status=status.HTTP_200_OK)
    





class SaveSaleRecordAPIView(APIView):
    

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]  # ✅ ผู้เข้าระหัสจึงสามารถที่จะทำการเข้าได้เท่านั้น 
   

    def post(self, request):
        try:
            data = request.data

            # ✅ ตรวจสอบ JSON
            stock_adjustments = data.get("stockAdjustments")
            if isinstance(stock_adjustments, str):
                try:
                    stock_adjustments = json.loads(stock_adjustments)
                except json.JSONDecodeError:
                    return Response({"error": "Invalid JSON format for stock_adjustments"}, status=status.HTTP_400_BAD_REQUEST)

            # ✅ บันทึกข้อมูลลง SaleRecord
            sale_record = SaleRecord.objects.create(
                total_amount=data["totalAmount"],
                entered_amount=data["enteredAmount"],
                change=data["change"],
                timestamp=datetime.fromisoformat(data["timestamp"]),
                stock_adjustments=data["stockAdjustments"],
                cashier=request.user
            )

            # ✅ รีเฟรชจากฐานข้อมูลให้แน่ใจว่าข้อมูลล่าสุด
            sale_record.refresh_from_db()

            # ✅ ส่งข้อมูลกลับไปให้ JavaScript ใช้งาน
            return Response({
                "message": "Sale record saved successfully!",
                "totalAmount": sale_record.total_amount,
                "enteredAmount": sale_record.entered_amount,
                "change": sale_record.change,
                "timestamp": sale_record.timestamp.isoformat(),
                "stockAdjustments": sale_record.stock_adjustments
            }, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({"error": f"Missing key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




#------------------------------------------------------------------------------------------------------------------------






@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin,login_url='/eror404/')
def apps_ecommerceCart(request):
    
    
     # ✅ เผื่อไว้ก่อนว่าตอน GET อาจยังไม่มี items (จาก POST)
    items = []

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("📦 Raw Data:", data)

            items = data.get("items", [])
            print(f"🧾 จำนวนรายการ: {len(items)}")

            total = 0.0
            for index, item in enumerate(items, start=1):
                print(f"👉 รายการ {index}: {item}")
                print("รายกาสำหรับแสดงค่าตัวแปล",item)
               
 
                raw_total = str(item.get("total", "0")).replace("บาท", "").replace(",", "").strip()
                try:
                    total += float(raw_total)
                except ValueError:
                    print(f"❌ ไม่สามารถแปลงค่า total เป็นตัวเลข: {raw_total}")

            print(f"💰 ยอดรวมทั้งหมด: {total:.2f} บาท")

            return JsonResponse({
                "message": "✅ ได้รับข้อมูลแล้ว",
                "total": f"{total:,.2f}", 
                "item_count": len(items),
            })
       
        except Exception as e:
            print("❌ Error:", str(e))
            return JsonResponse({"error": "เกิดข้อผิดพลาด", "detail": str(e)}, status=400)
    

    

     # เพิ่มสำหรับการแจ้งเตือน
   #Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
    # ✅ ดึงสินค้ายอดนิยม (Trending Products)
    Products = Product1.objects.filter(is_trending=True)
    
    # ✅ ดึงข้อมูลหมวดหมู่ทั้งหมด
    filter2 = Category.objects.all()
    
    # ✅ รับค่าพารามิเตอร์จาก `GET` Request
    category_id = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    sort_by = request.GET.get('sort', 'default')
  
    search = request.GET.get('search', None)  # ค่าจาก input 'searchBarcode'
    
    # ✅ Debug: แสดงค่าที่ได้รับจาก Query Parameters
    #print(f"🟢 Category ID: {category_id}, Min Price: {min_price}, Max Price: {max_price}, Sort: {sort_by}")


    # ✅ ดึงข้อมูลสินค้าทั้งหมด
    products = Product1.objects.all()
    
    
     #สำหรับการแจ้งเตือน
    ProductStock = Product1.objects.filter(stock__lt=10)  
    total_product_count = ProductStock.count()
    #print ("การนับข้อมูล",total_product_count);
    
    
   
    
    
    # ✅ทำการส่ง Ajax ไป
    
     # รับค่าพารามิเตอร์จาก `GET` Request
    category_id = request.GET.get('category', None)
    
     # ✅ กรองสินค้าตามหมวดหมู่
    if category_id and category_id.isdigit():
        products = products.filter(category_id=int(category_id))
        #print(f"✅ Filtered by Category ({category_id}): {products.count()} items found")
        
    
    # กรองตามช่วงราคา
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
     
     
      # ค้นหาตาม ID หรือ Barcode
 
        '''
    if search:
        # ตรวจสอบว่า search เป็นตัวเลข (หรือ id) หรือไม่
        if search.isdigit():
            # กรองสินค้าตาม id หรือ barcode
            products = products.filter(id=search) | products.filter(barcode=search)
            #print(f"✅ Filtering by ID or Barcode: {products.count()} items found")
        else:
            # หากไม่ใช่ตัวเลข ก็อาจจะเป็นชื่อ หรือคำค้นหาอื่นๆ ที่สามารถกรองได้
            products = products.filter(name__icontains=search)  # ตัวอย่างการค้นหาชื่อสินค้าด้วย `icontains`
           # print(f"✅ Filtering by Name or other: {products.count()} items found")
         '''
        
    '''if search:
        search = search.strip()  # ตัดช่องว่าง/อักขระพิเศษจากการยิงบาร์โค้ด
        if search.isdigit():
            products = products.filter(barcode=search)
        else:
        # ถ้าไม่ใช่ตัวเลข ให้ไม่แสดงอะไร
            products = products.none()
        print(f"🔍 search = '{search}'")'''
    
#--------------------------------------------------ถ้าคุณอยากให้การค้นหาสามารถพิมพ์แค่ บางส่วนของ barcode (โดยเฉพาะตัวหน้า) แล้วแสดงผลลัพธ์ที่ตรงกับตัวหน้าของ--------------------------------
    if search:
        search = search.strip()
        if search.isdigit():
        # ใช้ __startswith เพื่อค้นหา barcode ที่ขึ้นต้นด้วย search
            products = products.filter(barcode__startswith=search)
        else:
            products = products.none()
        print(f"🔍 search = '{search}'")



        
    # เรียงลำดับตามตัวเลือก
    if sort_by == 'highest':
        products = products.order_by('-price')
    elif sort_by == 'lowest':
        products = products.order_by('price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
        
        
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'apps-ecommerceCartAjax.html', {'products': products})  # ✅ แก้โค้ดปิด {} ค่อยมาไหล่ดูอีกทีหนึ่งแล้วกัน
     
        
        
    
    # ✅ กรองสินค้าตามช่วงราคา (ตรวจสอบค่าก่อนแปลงเป็น `float`)
    try:
        if min_price:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
           #print(f"✅ Filtered by Min Price ({min_price}): {products.count()} items found")

        if max_price:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
            #print(f"✅ Filtered by Max Price ({max_price}): {products.count()} items found")

    except ValueError:
        print("⚠️ Warning: ราคาไม่ใช่ตัวเลขที่ถูกต้อง")
    
    
    
    
    
    # ✅ เรียงลำดับสินค้าตามตัวเลือก
    if sort_by == 'highest':
        products = products.order_by('-price')  # ราคาสูงไปต่ำ
        #print("✅ Sorted by Highest Price")
    elif sort_by == 'lowest':
        products = products.order_by('price')  # ราคาต่ำไปสูง
        #print("✅ Sorted by Lowest Price")
    elif sort_by == 'newest':
        products = products.order_by('-created_at')  # สินค้าใหม่สุด
        #print("✅ Sorted by Newest")
        
     # ✅ Debug: ตรวจสอบจำนวนสินค้าหลังจากกรอง
    #print(f"🔵 Total Products After Filtering: {products.count()}")
    

    
    return render (request,"apps-ecommerceCart.html",{
        "Products": Products,  # ✅ สินค้ายอดนิยม
        "products": products,  # ✅ สินค้าทั้งหมด (ที่ถูกกรองแล้ว)
        "filter1": Product1.objects.all(),  # ✅ ข้อมูลสินค้าทั้งหมด
        "filter2": filter2,    # ✅ หมวดหมู่ทั้งหมด
        "categories": Category.objects.all(),  # ✅ หมวดหมู่ทั้งหมด (อีกตัว)
        "ProductStock":ProductStock,
        "total_product_count":total_product_count,
        'search': search,
      
        }) #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป
    


    

def DashboardUser(request):
     return render (request,"dashboards-analytics.html") #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป
 


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.warning(request, "กรุณาใส่ข้อมูลให้ครบ")
            return redirect("login_cover")

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
            return redirect("eror404")
        
        

        auth.login(request, user)
        return redirect("LayoutDashbords")  # เปลี่ยนเส้นทางไปยังหน้าแรก

        
        
    return render(request, "index.html")
 



@login_required(login_url='/login_cover/')
@user_passes_test(has_permission)

def LayoutDashbords(request):
    #print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    #print(f"Checking Group: {request.user.groups.all()}")

    # ✅ ดึง QuerySet ปกติ เพื่อให้ใช้ .image.url ได้
    ProductStock = Product1.objects.filter(stock__lt=10)  
    total_product_count = ProductStock.count()

    #print("การนับข้อมูล", total_product_count)
   # print("ดึงค่ารายการมา", ProductStock)

    return render(request, "LayoutDashbords.html", {"ProductStock": ProductStock, "total_product_count": total_product_count})



def appsinvoiceList(request):
    return render (request,"apps-invoiceList.html")
 
def eror404(request):
    return render (request,"404error.html")


def LayoutDashbords1(request):
    return render (request,"LayoutDashbords1.html")


def Calender(request):
     return render (request,"Calender1.html") #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป
 

@login_required(login_url='/eror404/')  #ถ้าคุณเข้าไปในตัวเว็บเพจเลยไปที่ url itemProductคุณจะไม่สามารถเรียกเข้าได้ คุณต้องผ่านการlogin ก่อนจึงสามารถที่จะทำการเข้าได้ ถ้าไม่ทำการ login ก็จะเข้าไปที่หน้า eror404
@user_passes_test(is_special_admin,login_url='/eror404/')
def ItemProduct(request):
    
       # รับค่าช่วงวันที่จาก GET request
    bangkok_tz = pytz.timezone("Asia/Bangkok")
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    
    
   
     
     #ทำการแจ้งเตือนสินค่า
    ProductStock = Product1.objects.filter(stock__lt=10)  
    total_product_count = ProductStock.count()
   # print ("การนับข้อมูล",total_product_count);
    
    #เพิ่มสำหรับการแจ้งเตือน
    #ProductStock = Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
  
    # ดึงข้อมูลทั้งหมดถ้าไม่มีการกรอง
    records = SaleRecord.objects.all().order_by('-timestamp')

    # ตรวจสอบว่าผู้ใช้กรอกวันที่ครบทั้งสองช่องหรือไม่
    if not start_date or not end_date:
        #messages.error(request, "กรุณากรอกวันที่ให้ครบทั้งสองช่อง!")  # ✅ แจ้งเตือน
        return render(request, "ItemProduct.html", {
            "records": [],
            "total_sum": 0,
            "total_profit_sum": 0,
            "start_date": start_date or "",
            "end_date": end_date or "",
            "ProductStock":ProductStock,
            "total_product_count":total_product_count,
        })

    try:
        # แปลงวันที่จาก string เป็น datetime object
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

        # ตรวจสอบว่าวันที่เริ่มต้นต้องไม่มากกว่าวันที่สิ้นสุด
        if start_date_obj > end_date_obj:
            messages.error(request, "วันที่เริ่มต้นต้องไม่มากกว่าวันที่สิ้นสุด!")
            return render(request, "ItemProduct.html", {
                "records": [],
                "total_sum": 0,
                "total_profit_sum": 0,
                "start_date": start_date,
                "end_date": end_date,
                "ProductStock":ProductStock,
                "total_product_count":total_product_count,
            })

        # ดึงข้อมูลที่อยู่ในช่วงวันที่ที่เลือก
        records = SaleRecord.objects.filter(timestamp__date__range=[start_date_obj, end_date_obj]).order_by('-timestamp')
       
        # คำนวณผลรวมยอดขาย
        total_sum = records.aggregate(total=Sum("total_amount"))["total"] or 0
        
          # ดึกข้อมูลจาก Stockadjustment เพื่อที่จะทำการรวม Total ของจำนวณ
        total_profit_sum = sum(sum(float(item.get("totalProfit") or 0) for item in record.stock_adjustments or [])for record in records if record.stock_adjustments)


       

    except ValueError:
        messages.error(request, "รูปแบบวันที่ไม่ถูกต้อง! กรุณากรอกเป็น YYYY-MM-DD")
        return render(request, "ItemProduct.html", {
            "records": [],
            "total_sum": 0,
            "total_profit_sum": 0,
            "start_date": start_date,
            "end_date": end_date,
            "ProductStock":ProductStock,
            "total_product_count":total_product_count,
        })

    return render(request, "ItemProduct.html", {
        "records": records,
        "total_sum": total_sum,
        "total_profit_sum": total_profit_sum,
        "start_date": start_date_obj.strftime('%d/%m/%Y'),
        "end_date": end_date_obj.strftime('%d/%m/%Y'),
        "ProductStock":ProductStock,
        "total_product_count":total_product_count,
    })





def logout_cover(request):
   # print(f"Before Logout - User: {request.user}")  # Debug ก่อน Logout
    auth.logout(request)
    request.session.flush()  # ✅ ล้าง Session ให้หมด
    print(f"After Logout - User: {request.user}")  # Debug หลัง Logout
    return redirect("login_cover")









def login_cover(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.warning(request, "กรุณาใส่ข้อมูลให้ครบ")
            return redirect("login_cover")

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
            return redirect("eror404")
        
        

        auth.login(request, user)
        return redirect("LayoutDashbords")  # เปลี่ยนเส้นทางไปยังหน้าแรก

        
        
    return render(request, "login-cover.html")
 
def register_cover(request):
    return render(request,"register-cover.html") # สำหรับการามัครสมาชิก
 

@login_required(login_url='/login_cover/') # สำหรับการามัครสมาชิก
@user_passes_test(is_special_admin,login_url='/eror404/') # ถ้าไม่ได้อนุญาติก็จะdirect ไปที่ urlนั้ อนุญาติเข้าสู่ระบบโดยกลุ่มนี้นอกเหนือจากกลุ่มนั้ก็ไม่สามารถเข้าไปได้
def EditAdd(request,id):
    
    
    product = get_object_or_404(Product1, pk=id)
    filter2 = Category.objects.all()
    
    filter1= Product1.objects.all()
    filter2=Category.objects.all()
    product=Product1.objects.get(pk=id)
    
    
    #สำหรับการแจ้งเตือนสินค้า
    ProductStock = Product1.objects.filter(stock__lt=10)  
    total_product_count = ProductStock.count()
   # print ("การนับข้อมูล",total_product_count);
    
    #เพิ่มสำหรับการแจ้งเตือน
   # ProductStock = Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
    
    if request.method == "POST":
       # print(request.POST)  # ✅ Debug ตรวจสอบข้อมูลที่ส่งมา

        # ✅ รับค่าจากฟอร์ม
        product_name = request.POST.get("product_name", "").strip()
        product_price = request.POST.get("product_price", "").strip()
        stock = request.POST.get("stock", "").strip()
        profitprice = request.POST.get("profitprice", "").strip()
        barcode = request.POST.get("barcode", "").strip()
        category_id = request.POST.get("taxApplicable", "").strip()
        description = request.POST.get("productDescription", "").strip()

        # ✅ ตรวจสอบค่าห้ามว่าง
        if not product_name or not product_price or not stock or not profitprice or not barcode:
            return render(request, "ProductPreview.html", {
                "product": product,
                "filter2": filter2,
                "error": "กรุณากรอกข้อมูลให้ครบทุกช่อง"
            })

        try:
            product_price = Decimal(product_price)
            stock = Decimal(stock)
            profitprice = Decimal(profitprice)
        except InvalidOperation:
            return render(request, "ProductPreview.html", {
                "product": product,
                "filter2": filter2,
                "error": "ข้อมูลที่กรอกต้องเป็นตัวเลขเท่านั้น"
            })

        # ✅ อัปเดตข้อมูลสินค้า
        product.name = product_name
        product.price = product_price
        product.stock = stock
        product.profitprice = profitprice
        product.barcode = barcode
        product.description = description

        if category_id:
            try:
                product.category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                return render(request, "ProductPreview.html", {
                    "product": product,
                    "filter2": filter2,
                    "error": "ประเภทสินค้าที่เลือกไม่มีอยู่ในระบบ"
                })

        product.save()
        return redirect("EditAdd", id=product.id)
    
    
    return render (request,"EditAdd.html",{"product":product,"filter1":filter1,"filter2":filter2,"ProductStock":ProductStock,"total_product_count":total_product_count})




@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin, login_url='/eror404/')
def ProductPreview(request):
    """
    แสดงรายการสินค้าทั้งหมด พร้อมตัวกรองและการเรียงลำดับ
    """

    # ✅ เรียกสินค้าทั้งหมดไว้ก่อนสำหรับบาง context
    product = Product1.objects.all()

    # ✅ กำหนดตัวแปร products สำหรับกรอง
    products = Product1.objects.all()

    # 🔍 ค้นหาด้วย Barcode
    search = request.GET.get('search', '').strip()
    if search:
        if search.isdigit():
            products = products.filter(barcode__startswith=search)
        else:
            products = Product1.objects.none()

    # ✅ ดึงสินค้ายอดนิยม
    Products = Product1.objects.filter(is_trending=True)

    # ✅ ดึงข้อมูลหมวดหมู่ทั้งหมด
    filter2 = Category.objects.all()

    # ✅ รับค่าจาก URL สำหรับการกรอง
    category_id = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    sort_by = request.GET.get('sort', 'default')

    # ✅ กรองตามหมวดหมู่
    if category_id and category_id.isdigit():
        products = products.filter(category_id=int(category_id))

    # ✅ กรองตามช่วงราคา
    try:
        if min_price:
            products = products.filter(price__gte=float(min_price))
        if max_price:
            products = products.filter(price__lte=float(max_price))
    except ValueError:
        print("⚠️ Warning: ราคาไม่ใช่ตัวเลขที่ถูกต้อง")

    # ✅ เรียงลำดับสินค้า
    if sort_by == 'highest':
        products = products.order_by('-price')  # ราคาสูง -> ต่ำ
    elif sort_by == 'lowest':
        products = products.order_by('price')   # ราคาต่ำ -> สูง
    elif sort_by == 'newest':
        products = products.order_by('-created_at')  # ล่าสุด -> เก่าสุด

    # ✅ ดึงสินค้าที่ stock น้อยกว่า 10
    ProductStock = Product1.objects.filter(stock__lt=10)
    total_product_count = ProductStock.count()

    # ✅ ส่งข้อมูลไปยัง template
    return render(request, "ProductPreview.html", {
        "Products": Products,                     # สินค้ายอดนิยม
        "products": products,                     # สินค้าที่ผ่านการกรอง
        "filter1": Product1.objects.all(),        # สำหรับ dropdown
        "filter2": filter2,                        # หมวดหมู่
        "categories": Category.objects.all(),     # หมวดหมู่ (อีกตัว)
        "ProductStock": ProductStock,             # สินค้าใกล้หมด
        "total_product_count": total_product_count,
        "product": product,                       # ทั้งหมด (original)
    })



@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin,login_url='/eror404/')
def update_product_price_stock(request, pk):
    if request.method == "POST":
        product = Product1.objects.get(id=pk)
        
        product.price = request.POST.get("product_price")
        product.stock = request.POST.get("product_stock")  # ← ต้องได้ค่า ไม่ใช่ None

        if not product.stock:
            return HttpResponse("Stock is empty or missing", status=400)

        product.save()

        return redirect(reverse('ProductPreview'))





@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin,login_url='/eror404/')
def Circulation1(request):
    # รับค่าช่วงวันที่จาก GET request
    bangkok_tz = pytz.timezone("Asia/Bangkok")
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    #เพิ่มสำหรับการแจ้งเตือน
    ProductStock = Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
    # ดึงข้อมูลทั้งหมดถ้าไม่มีการกรอง
    records = SaleRecord.objects.all().order_by('-timestamp')
    # เพิ่มสำหรับการแจ้งแตือน
    ProductStock = Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
    # ตรวจสอบว่าผู้ใช้กรอกวันที่ครบทั้งสองช่องหรือไม่
    
    
    #สำหรับการแจ้งเตือน
    ProductStock = Product1.objects.filter(stock__lt=10)  
    total_product_count = ProductStock.count()
    print ("การนับข้อมูล",total_product_count);
    
    if not start_date or not end_date:
        messages.error(request, "กรุณากรอกวันที่ให้ครบทั้งสองช่อง!")  # ✅ แจ้งเตือน
        return render(request, "Circulation.html", {
            "records": [],
            "total_sum": 0,
            "start_date": start_date or "",
            "end_date": end_date or ""
        })

    try:
        # แปลงวันที่จาก string เป็น datetime object
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

        # ตรวจสอบว่าวันที่เริ่มต้นต้องไม่มากกว่าวันที่สิ้นสุด
        if start_date_obj > end_date_obj:
            messages.error(request, "วันที่เริ่มต้นต้องไม่มากกว่าวันที่สิ้นสุด!")
            return render(request, "Circulation.html", {
                "records": [],
                "total_sum": 0,
                "start_date": start_date,
                "end_date": end_date
            })

        # ดึงข้อมูลที่อยู่ในช่วงวันที่ที่เลือก
        records = SaleRecord.objects.filter(timestamp__date__range=[start_date_obj, end_date_obj]).order_by('-timestamp')

        # คำนวณผลรวมยอดขาย
        total_sum = records.aggregate(total=Sum("total_amount"))["total"] or 0

    except ValueError:
        messages.error(request, "รูปแบบวันที่ไม่ถูกต้อง! กรุณากรอกเป็น YYYY-MM-DD")
        return render(request, "Circulation.html", {
            "records": [],
            "total_sum": 0,
            "start_date": start_date,
            "end_date": end_date
        })

    return render(request, "Circulation.html", {
        "records": records,
        "total_sum": total_sum,
        "start_date": start_date_obj.strftime('%d/%m/%Y'),
        "end_date": end_date_obj.strftime('%d/%m/%Y'),
        "ProductStock":ProductStock,
        "total_product_count":total_product_count,
    })


@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin,login_url='/eror404/')

def Circulation2(request):
    
    filter_type = request.GET.get("filter", "year")  
    today = now()  # ✅ ใช้ timezone-aware datetime
    bangkok_tz = pytz.timezone("Asia/Bangkok")
    today = today.astimezone(bangkok_tz)
    
    if filter_type == "day":
        start_date = today  # ✅ ใช้วันนี้เลย
    elif filter_type == "week":
        start_date = today - timedelta(weeks=1)
    elif filter_type == "month":
        start_date = today - timedelta(days=30)
    elif filter_type == "3months":
        start_date = today - timedelta(days=90)
    elif filter_type == "6months":
        start_date = today - timedelta(days=180)
    else:  # "year"
        start_date = today - timedelta(days=365)
        

    ProductStock = Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
    
    
    # ค่าที่แสดงในการรวมมูลล่ะค่าของร้าน
    TotlalShop = list(Product1.objects.values("name", "price", "stock"))
    #print("รวมมูลค่าของที่อยู่ในร้านทั้งหมด:",TotlalShop);
    total_valueShop = round(sum(item["price"] * item["stock"] for item in TotlalShop), 2)


    #print("ราคารวมทั้งหมด:",total_valueShop)


    
  
    
    # ✅ รีเซ็ตเวลาเป็น 00:00:00 เพื่อให้ได้ข้อมูลตั้งแต่ต้นวัน
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = today.replace(hour=23, minute=59, second=59, microsecond=999999)

    
    #print(f"🟢 filter_type: {filter_type}")
    #print(f"🕒 start_date: {start_date} → end_date: {end_date}")
    #print(f"🟢 filter_type: {filter_type}")
    #print(f"🕒 start_date: {start_date}")
    
    # ✅ ดึงข้อมูลที่อยู่ในช่วงเวลาที่เลือก
    records1 = SaleRecord.objects.filter(timestamp__gte=start_date).order_by('-timestamp')
    # ✅ หาผลรวมของ total_amount
    total_sum = records1.aggregate(total=Sum("total_amount"))["total"] or 0  
    # หาผลรวมรายวัน รายเดือนของ Totalsum
    daily_sales = records1.annotate(date=TruncDate('timestamp')).values('date').annotate(total=Sum('total_amount')).order_by('date') # total amout มาจาก model 
    weekly_sales = records1.annotate(week=TruncWeek('timestamp')).values('week').annotate(total=Sum('total_amount')).order_by('week')
    monthly_sales = records1.annotate(month=TruncMonth('timestamp')).values('month').annotate(total=Sum('total_amount')).order_by('month')

    # ✅ ------------------------------------------------------------ดึงข้อมูลรายวัน, รายสัปดาห์, รายเดือน (กำไร)
   
    
    bangkok_tz = pytz.timezone("Asia/Bangkok")

# ✅ ใช้ defaultdict(float) เพื่อเก็บค่ากำไรแยกตามวัน, สัปดาห์, เดือน
    daily_profit = defaultdict(float)
    weekly_profit = defaultdict(float)
    monthly_profit = defaultdict(float)

    # ✅ เรียง records1 ตามวันที่ (ไทย) เพื่อให้ groupby ทำงานถูกต้อง
    records1 = sorted(records1, key=lambda r: r.timestamp.astimezone(bangkok_tz).date())

# ✅ ใช้ groupby เพื่อจัดกลุ่มตามวันที่
    for date, records_iter in groupby(records1, key=lambda r: r.timestamp.astimezone(bangkok_tz).date()):
        records = list(records_iter)  # ✅ แปลง iterator เป็น list
        total_profit_per_day = 0  # ✅ กำหนดให้ทุกวันเริ่มนับใหม่

        for record in records:
            timestamp_th = record.timestamp.astimezone(bangkok_tz)
            week = timestamp_th.isocalendar()[1]
            month = timestamp_th.strftime("%Y-%m")

            # ✅ ตรวจสอบ stock_adjustments เป็น JSON หรือไม่
            stock_adjustments = record.stock_adjustments
            if isinstance(stock_adjustments, str):
                try:
                    stock_adjustments = json.loads(stock_adjustments)
                except json.JSONDecodeError:
                    stock_adjustments = []  # ✅ ป้องกัน Error กรณี JSON ไม่ถูกต้อง

        # ✅ รวมกำไรของวันนั้น (ไม่สะสมวันก่อนหน้า)
            for item in stock_adjustments:
                if isinstance(item, dict):
                    total_profit = float(item.get("totalProfit") or 0)
                    total_profit_per_day += total_profit  # ✅ รวมกำไรของวันนั้น

    # ✅ บันทึกค่าแบบรายวัน (ไม่สะสม)
        daily_profit[date] = total_profit_per_day
        weekly_profit[week] += total_profit_per_day  # ✅ ยังสะสมรายสัปดาห์
        monthly_profit[month] += total_profit_per_day  # ✅ ยังสะสมรายเดือน

# ✅ แปลงเป็น List สำหรับ JSON Response
    daily_profit_list = [{"date": str(date), "total": total} for date, total in daily_profit.items()]
    weekly_profit_list = [{"week": week, "total": total} for week, total in weekly_profit.items()]
    monthly_profit_list = [{"month": month, "total": total} for month, total in monthly_profit.items()]

# ✅ DEBUG แสดงค่า JSON ที่ได้
    #print("✅ [DEBUG] แสดงค่ารายวัน (sum):", daily_profit_list)
    #print("✅ [DEBUG] แสดงค่ารายสัปดาห์ (sum):", weekly_profit_list)
    #print("✅ [DEBUG] แสดงค่ารายเดือน (sum):", monthly_profit_list)
    
    #--------------------------------------------------------------------------------endingกราฟ-------------------------------------------------
    
    
   # สำหรับการแสดงการแจ้งเตือน
    ProductStock = Product1.objects.filter(stock__lt=10)  
    total_product_count = ProductStock.count()
    #print ("การนับข้อมูล",total_product_count);
    
     
    
    

    
    # ทำการดึงข้อมูลรายการรวมทั้งหมดออกมาไม่ว่าจะเป็นรวมยอดขายหรือทำการรวมกำไร 
    sale_records = SaleRecord.objects.all()
    
  
    # ✅ รวมยอดขายทั้งหมด
    total_profit = sum([sum(float(item.get("totalProfit") or 0.0) for item in record.stock_adjustments) for record in sale_records if record.stock_adjustments])


    total_price = sum([
        sum(item.get("TotalPrice", 0) for item in record.stock_adjustments)
        for record in sale_records])

    # ✅ กรองข้อมูลยอดขายเป็นรายวัน รายสัปดาห์ และรายเดือน ของยอดขายดี
    # ✅ กรองยอดขายรวมตามวัน, สัปดาห์, เดือน
    # ✅ จัดกลุ่มสินค้าให้รวมยอดขายของสินค้าที่ชื่อเดียวกัน
    product_sales = defaultdict(float)
    
    #print(f"✅ จำนวน Record ที่ดึงมา: {len(records1)}")

    for record in records1:
         
        
          for item in record.stock_adjustments:
            product_sales[item["product"]] += item["quantity"] 
     # ✅ แปลงข้อมูลเป็น JSON พร้อมเรียงจากสินค้าขายดีที่สุด
    sorted_product_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    product_sales_json = [{"x": product, "y": quantity} for product, quantity in sorted_product_sales]
    
    
           # ✅ ดึงข้อมูลจาก Database
    records1 = SaleRecord.objects.filter(timestamp__gte=start_date).order_by('-timestamp') 
  # ✅ ตรวจสอบว่าผู้ใช้ต้องการ JSON หรือ HTML
    if request.headers.get('Accept') == 'application/json' or request.GET.get("format") == "json":
        sales_data = [
        {   
         
            "totalProfit": sum(float(item.get("totalProfit") if item.get("totalProfit") is not None else 0.0) for item in record.stock_adjustments),
            "TotalPrice": sum(float(item.get("TotalPrice", 0.0)) for item in record.stock_adjustments),  # ✅ รวม TotalPriceต่อจากนี้เดียวทำการแก้ไขอยู่ในนี้------------------
            "timestamp": record.timestamp.astimezone(bangkok_tz).strftime("%d-%m-%y %H:%M:%S"),  # ✅ แปลงเป็นเวลาไทย
            "total_amount": float(record.total_amount),  # ✅ แปลงเป็น float
            "stock_adjustments": [
                {
                    "product": item["product"],
                    "quantity": float(item["quantity"]),  # ✅ แปลงเป็น float
                    "totalProfit": float(item.get("totalProfit") if item.get("totalProfit") is not None else 0.0),
                    "TotalPrice": float(item.get("TotalPrice", 0.0)),                                    
                }
                for item in record.stock_adjustments
            ]
            
            
        }
        for record in records1
        ]
        
         # ✅ ทำการรวมข้อมูลใน Sale_data
        filtered_totalProfit = sum(sale.get("totalProfit", 0.0) for sale in sales_data)
        filtered_totalPrice = sum(sale.get("TotalPrice", 0.0) for sale in sales_data)
        
            # ✅ แปลง product_sales_json ให้เป็นตัวเลข
        product_sales_json = [
        {"x": product, "y": float(quantity)}  # ✅ แปลงเป็น float
        for product, quantity in sorted_product_sales
            ]
        
        
        #การดึงข้อมูลจาก json ----------------------------------------------------------------------------------------------------
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        #การดึงข้อมูลจาก json ----------------------------------------------------------------------------------------------------
        
        
         # ตัวนี้ Return API Json 
        return JsonResponse({
            
            "total_sum": float(total_sum),
            "totalProfit1": round(filtered_totalProfit, 2),
            "totalPrice1": round(filtered_totalPrice, 2),
            "totalProfit": round(total_profit, 2),
            "TotalPrice": round(total_price, 2),
            "start_date": start_date.strftime("%d-%m-%y"),
            "end_date": end_date.strftime("%d-%m-%y"),
            "sales": sales_data,
            "product_sales": product_sales_json,
            "daily_sales": list(daily_sales) if daily_sales else [],
            "weekly_sales": list(weekly_sales) if weekly_sales else [],
            "monthly_sales": list(monthly_sales) if monthly_sales else [],
            "daily_profit1": daily_profit_list,
            "weekly_profit1": weekly_profit_list,
            "monthly_profit1": monthly_profit_list,
            "total_valueShop":total_valueShop,
            
          
      
           
            }, 
            safe=False, json_dumps_params={'ensure_ascii': False})



  # ตัวนี้ Return สำหรับการเอาค่าไปแสดงที่หน้าจอ 
    return render(request, "dashboards-analytics.html", {
        "records1": records1,
        "total_sum": total_sum,
        "totalProfit": round(total_profit, 2),
        "TotalPrice": round(total_price, 2),
        "filter_type": filter_type,
        "product_sales_json": product_sales_json,
        "ProductStock":ProductStock,
        "total_product_count":total_product_count,
        "total_valueShop":total_valueShop,
       
    })
    
    
   
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    


def Circulation3(request):
        # รับค่าจาก GET parameter
    filter_type = request.GET.get("filter", "year")  # ค่าเริ่มต้นเป็น "year"
    
    today = datetime.now()
    
    if filter_type == "day":
        start_date = today - timedelta(days=1)
    elif filter_type == "week":
        start_date = today - timedelta(weeks=1)
    elif filter_type == "month":
        start_date = today - timedelta(days=30)
    elif filter_type == "3months":
        start_date = today - timedelta(days=90)
    elif filter_type == "6months":
        start_date = today - timedelta(days=180)
    else:  # "year"
        start_date = today - timedelta(days=365)
    
    # กรองข้อมูลตามช่วงเวลาที่เลือก
    records1 = SaleRecord.objects.filter(timestamp__gte=start_date).order_by('-timestamp')

    # หาผลรวมของ total_amount ตามช่วงที่เลือก
    total_sum = records1.aggregate(total=Sum("total_amount"))["total"] or 0  

    return render(request, "Circulation1.html", {
        "records1": records1,
        "total_sum": total_sum,
        "filter_type": filter_type  # ส่งค่า filter_type ไปยัง template
    })
    
    
    
def bestSeller(request):
     records1 = SaleRecord.objects.all()
     
     return render (request,"LayoutDashbords.html",records1=records1);
    
#ใช้สำหรับตรวจสอบข้อมูลว่าเป็น ชนิดของข้อมูลประเภทอะไร 
#for record in SaleRecord.objects.all(): 
#   print(record.stock_adjustments)


#ใช้สำหรับตรวจสอบข้อมูลว่าเป็น ชนิดของข้อมูลประเภทอะไร 
#for record in SaleRecord.objects.all(): 
#   print(record.total_amount);


#for record1 in SaleRecord.objects.all():
     
#     print(record1.stock_adjustments);


def check_time(request):
    return HttpResponse(f"เวลาปัจจุบันของ Django คือ: {now()}")

#-------------------------------------สำหรับดึงค่าใบกำกับภาษี------------------------------------------------------------


def load_products(request):
    category_id = request.GET.get('category_id')
    products = Product1.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(products.values('id', 'name')), safe=False)

