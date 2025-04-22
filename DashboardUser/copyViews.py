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




def DashboardUser(request):
     return render (request,"dashboards-analytics.html") #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป

def LayoutDashbords(request):
     return render (request,"LayoutDashbords.html") #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป


def Calender(request):
     return render (request,"Calender1.html") #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป

def ItemProduct(request):
     return render (request,"ItemProduct.html")
 
def EditAdd(request,id):
    
    
    product = get_object_or_404(Product1, pk=id)
    filter2 = Category.objects.all()
    
    filter1= Product1.objects.all()
    filter2=Category.objects.all()
    product=Product1.objects.get(pk=id)
    
    if request.method == "POST":
        print(request.POST)  # ✅ Debug ตรวจสอบข้อมูลที่ส่งมา

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
            return render(request, "EditAdd.html", {
                "product": product,
                "filter2": filter2,
                "error": "กรุณากรอกข้อมูลให้ครบทุกช่อง"
            })

        try:
            product_price = Decimal(product_price)
            stock = Decimal(stock)
            profitprice = Decimal(profitprice)
        except InvalidOperation:
            return render(request, "EditAdd.html", {
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
                return render(request, "EditAdd.html", {
                    "product": product,
                    "filter2": filter2,
                    "error": "ประเภทสินค้าที่เลือกไม่มีอยู่ในระบบ"
                })

        product.save()
        return redirect("EditAdd", id=product.id)
    
    
    return render (request,"EditAdd.html",{"product":product,"filter1":filter1,"filter2":filter2})

def ProductPreview(request):
    """
    แสดงรายการสินค้าทั้งหมด พร้อมตัวกรองและการเรียงลำดับ
    """

    # ✅ ดึงสินค้ายอดนิยม (Trending Products)
    Products = Product1.objects.filter(is_trending=True)

    # ✅ ดึงข้อมูลหมวดหมู่ทั้งหมด
    filter2 = Category.objects.all()

    # ✅ รับค่าพารามิเตอร์จาก `GET` Request
    category_id = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    sort_by = request.GET.get('sort', 'default')

    # ✅ Debug: แสดงค่าที่ได้รับจาก Query Parameters
    print(f"🟢 Category ID: {category_id}, Min Price: {min_price}, Max Price: {max_price}, Sort: {sort_by}")

    # ✅ ดึงข้อมูลสินค้าทั้งหมด
    products = Product1.objects.all()

    # ✅ กรองสินค้าตามหมวดหมู่
    if category_id and category_id.isdigit():
        products = products.filter(category_id=int(category_id))
        print(f"✅ Filtered by Category ({category_id}): {products.count()} items found")

    # ✅ กรองสินค้าตามช่วงราคา (ตรวจสอบค่าก่อนแปลงเป็น `float`)
    try:
        if min_price:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
            print(f"✅ Filtered by Min Price ({min_price}): {products.count()} items found")

        if max_price:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
            print(f"✅ Filtered by Max Price ({max_price}): {products.count()} items found")

    except ValueError:
        print("⚠️ Warning: ราคาไม่ใช่ตัวเลขที่ถูกต้อง")

    # ✅ เรียงลำดับสินค้าตามตัวเลือก
    if sort_by == 'highest':
        products = products.order_by('-price')  # ราคาสูงไปต่ำ
        print("✅ Sorted by Highest Price")
    elif sort_by == 'lowest':
        products = products.order_by('price')  # ราคาต่ำไปสูง
        print("✅ Sorted by Lowest Price")
    elif sort_by == 'newest':
        products = products.order_by('-created_at')  # สินค้าใหม่สุด
        print("✅ Sorted by Newest")

    # ✅ Debug: ตรวจสอบจำนวนสินค้าหลังจากกรอง
    print(f"🔵 Total Products After Filtering: {products.count()}")

    # ✅ ส่งข้อมูลไปยัง Template
    return render(request, "ProductPreview.html", {
        "Products": Products,  # ✅ สินค้ายอดนิยม
        "products": products,  # ✅ สินค้าทั้งหมด (ที่ถูกกรองแล้ว)
        "filter1": Product1.objects.all(),  # ✅ ข้อมูลสินค้าทั้งหมด
        "filter2": filter2,    # ✅ หมวดหมู่ทั้งหมด
        "categories": Category.objects.all(),  # ✅ หมวดหมู่ทั้งหมด (อีกตัว)
    })





def Circulation1(request):
    # รับค่าช่วงวันที่จาก GET request
    bangkok_tz = pytz.timezone("Asia/Bangkok")
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    # ดึงข้อมูลทั้งหมดถ้าไม่มีการกรอง
    records = SaleRecord.objects.all().order_by('-timestamp')

    # ตรวจสอบว่าผู้ใช้กรอกวันที่ครบทั้งสองช่องหรือไม่
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
        "end_date": end_date_obj.strftime('%d/%m/%Y')
    })


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


    # ✅ รีเซ็ตเวลาเป็น 00:00:00 เพื่อให้ได้ข้อมูลตั้งแต่ต้นวัน
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = today.replace(hour=23, minute=59, second=59, microsecond=999999)

    print(f"🟢 filter_type: {filter_type}")
    print(f"🕒 start_date: {start_date} → end_date: {end_date}")
    print(f"🟢 filter_type: {filter_type}")
    print(f"🕒 start_date: {start_date}")
    
    # ✅ ดึงข้อมูลที่อยู่ในช่วงเวลาที่เลือก
    records1 = SaleRecord.objects.filter(timestamp__gte=start_date).order_by('-timestamp')
    # ✅ หาผลรวมของ total_amount
    total_sum = records1.aggregate(total=Sum("total_amount"))["total"] or 0  
    # หาผลรวมรายวัน รายเดือนของ Totalsum
    daily_sales = records1.annotate(date=TruncDate('timestamp')).values('date').annotate(total=Sum('total_amount')).order_by('date') # total amout มาจาก model 
    weekly_sales = records1.annotate(week=TruncWeek('timestamp')).values('week').annotate(total=Sum('total_amount')).order_by('week')
    monthly_sales = records1.annotate(month=TruncMonth('timestamp')).values('month').annotate(total=Sum('total_amount')).order_by('month')

    # ✅ ------------------------------------------------------------ดึงข้อมูลรายวัน, รายสัปดาห์, รายเดือน (กำไร)
   
    
    daily_profit = {}
    weekly_profit = {}
    monthly_profit = {}

    for record in records1:
        # ✅ แปลง timestamp เป็น Date / Week / Month
        date = record.timestamp.date()  
        week = record.timestamp.isocalendar()[1]  
        month = record.timestamp.strftime("%Y-%m")

        # ✅ ตรวจสอบว่า stock_adjustments เป็น string JSON หรือไม่
        stock_adjustments = record.stock_adjustments
        if isinstance(stock_adjustments, str):
            stock_adjustments = json.loads(stock_adjustments)  # ✅ แปลงเป็น dict

        # ✅ ตรวจสอบค่า stock_adjustments ก่อนประมวลผล
        if not isinstance(stock_adjustments, list):
            print(f"⚠️ ข้อมูล stock_adjustments ผิดรูปแบบ: {stock_adjustments}")
            stock_adjustments = []  # ให้เป็น list ว่างเพื่อป้องกัน error

        # ✅ รวม totalProfit จาก stock_adjustments ที่มีค่า totalProfit เท่านั้น
        total_profit = sum(
            float(item["totalProfit"]) for item in stock_adjustments if isinstance(item, dict) and "totalProfit" in item)

        print("📅 เวลาสำหรับการทำงาน:", date)
        print("💰 ค่า totalProfit:", total_profit)

        # ✅ รวมกำไรต่อวัน
        daily_profit[date] = daily_profit.get(date, 0) + total_profit

        # ✅ รวมกำไรต่อสัปดาห์
        weekly_profit[week] = weekly_profit.get(week, 0) + total_profit

        # ✅ รวมกำไรต่อเดือน
        monthly_profit[month] = monthly_profit.get(month, 0) + total_profit

        # ✅ แปลงเป็น List สำหรับ JSON Response
    daily_profit_list = [{"date": str(date), "total": total} for date, total in daily_profit.items()]
    weekly_profit_list = [{"week": week, "total": total} for week, total in weekly_profit.items()]
    monthly_profit_list = [{"month": month, "total": total} for month, total in monthly_profit.items()]

    print("✅ แสดงค่ารายวันสำหรับกำไร:", daily_profit_list)
    print("✅ แสดงค่ารายปดาห์สำหรับกำไร:", weekly_profit_list)
    print("✅ แสดงค่ารายเดือนสำหรับกำไร:", monthly_profit_list)
    
    
    
    
    
    
    
    
    
    
    
    

    
    # ทำการดึงข้อมูลรายการรวมทั้งหมดออกมาไม่ว่าจะเป็นรวมยอดขายหรือทำการรวมกำไร 
    sale_records = SaleRecord.objects.all()
    # ✅ รวมยอดขายทั้งหมด
    total_profit = sum([
        sum(item.get("totalProfit", 0) for item in record.stock_adjustments)
        for record in sale_records
    ])

    total_price = sum([
        sum(item.get("TotalPrice", 0) for item in record.stock_adjustments)
        for record in sale_records
    ])

    # ✅ กรองข้อมูลยอดขายเป็นรายวัน รายสัปดาห์ และรายเดือน ของยอดขายดี
    # ✅ กรองยอดขายรวมตามวัน, สัปดาห์, เดือน
    # ✅ จัดกลุ่มสินค้าให้รวมยอดขายของสินค้าที่ชื่อเดียวกัน
    product_sales = defaultdict(float)
    
    print(f"✅ จำนวน Record ที่ดึงมา: {records1.count()}")
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
         
            "totalProfit": sum(float(item.get("totalProfit", 0.0)) for item in record.stock_adjustments),  # ✅ รวม totalProfit
            "TotalPrice": sum(float(item.get("TotalPrice", 0.0)) for item in record.stock_adjustments),  # ✅ รวม TotalPriceต่อจากนี้เดียวทำการแก้ไขอยู่ในนี้------------------
            "timestamp": record.timestamp.astimezone(bangkok_tz).strftime("%d-%m-%y %H:%M:%S"),  # ✅ แปลงเป็นเวลาไทย
            "total_amount": float(record.total_amount),  # ✅ แปลงเป็น float
            "stock_adjustments": [
                {
                    "product": item["product"],
                    "quantity": float(item["quantity"]),  # ✅ แปลงเป็น float
                    "totalProfit": float(item.get("totalProfit", 0.0)), 
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
          
      
           
            }, 
            safe=False, json_dumps_params={'ensure_ascii': False})



  # ตัวนี้ Return สำหรับการเอาค่าไปแสดงที่หน้าจอ 
    return render(request, "dashboards-analytics.html", {
        "records1": records1,
        "total_sum": total_sum,
         
        "totalProfit": round(total_profit, 2),
        "TotalPrice": round(total_price, 2),
        "filter_type": filter_type,
        "product_sales_json": product_sales_json
       
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