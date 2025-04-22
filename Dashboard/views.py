from django.shortcuts import render,redirect
from productapp.models import Product1,Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated  #ทำการติดเพื่อที่จะอนุญาตืให้ API ฝั่งjavascript ทำงานได้

from rest_framework.views import APIView # เรียกเข้า API View
from rest_framework.response import Response # เรียกเข้า API View
from rest_framework import status  # เรียกเข้า API View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from decimal import Decimal #ทำการแปลงค่าให้ตัวเลขอยู่ในรูปแบบทศนิยม

from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
#----------------------------------------------------importอันต่อไป---------------------------------

from .models import SaleRecord
import json
from datetime import datetime

#-----------------------------------------------------------ต่อไป------------------------------------
import qrcode
import base64
from io import BytesIO
from django.http import JsonResponse
import io
from django.contrib.auth.decorators import login_required,user_passes_test # สำหรับการส่งให้กับให้กับ user.ใน dashboard ต้องมีตัวนี้

from django.utils.timezone import make_aware
from django.utils import timezone  # ✅ นำเข้า timezone สำหรับจัดการโซนเวลา

from rest_framework.authentication import SessionAuthentication
from .authentication import CsrfExemptSessionAuthentication  # ✅ Import class ที่เราสร้าง คือต้องการที่จะทำการปิด csrf token


from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.


def ShowForDisplay(request):
    
    return render(request,"ShowForDisplay.html")


def Recipe(request):
    
    return render(request,"Recipe.html")



@login_required
def check_auth(request):
    return JsonResponse({"authenticated": True, "user": request.user.username})



def is_special_admin(user):
    return user.is_authenticated and user.groups.filter(name='Dashboards').exists()


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def product_list_ajax(request):
    
    return render(request,"product_list_ajax.html")


def get_product_list(request):
    products = list(Product1.objects.values("id", "name", "price", "stock", "barcode"))
    return JsonResponse({"products": products})


@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin)
def ShowDashBoard(request): 
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Checking Group: {request.user.groups.all()}")

    # เพิ่มสำหรับการแจ้งเตือน
    ProductStock = Product1.objects.filter(stock__lt=10).values("id", "name", "stock","updated_at")
    Products = Product1.objects.filter(is_trending=True)

    # ดึงข้อมูลวนลูบสำหรับหารายการสินค้า  
    all_product = Product1.objects.all().order_by("name")  # ดึงข้อมูลทั้งหมดที่เป็น Product1 
    print(f"Total Products: {all_product.count()}")  # Debug จำนวนสินค้า
    
    # ✅ ดึงสินค้าเฉพาะที่ stock < 10 และนับจำนวนสินค้าเหล่านั้น
    total_product_count = Product1.objects.filter(stock__lt=10).count()
    print ("การนับข้อมูล",total_product_count);
    
    # ✅ ดึงข้อมูลหมวดหมู่ทั้งหมด
    filter2 = Category.objects.all()
    
      # ✅ รับค่าพารามิเตอร์จาก `GET` Request
    categories = Category.objects.all()
    category_id = request.GET.get('category', None)
    
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    sort_by = request.GET.get('sort', 'default')

    print(f"🟢 Category ID: {category_id}, Min Price: {min_price}, Max Price: {max_price}, Sort: {sort_by}")
    
    
    # ✅ ดึงข้อมูลสินค้าทั้งหมด
    products = Product1.objects.all()
    
    
    
     # ✅ กรองสินค้าตามหมวดหมู่
    if category_id and category_id.isdigit():
        products = products.filter(category_id=int(category_id))
    
        print(f"✅ Filtered by Category ({category_id}): {products.count()} items found")

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'product_list_ajax.html', {'products': products})  # ✅ แก้โค้ดปิด {} ค่อยมาไหล่ดูอีกทีหนึ่งแล้วกัน
    
    
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
    
    
    
    return render(request, 
                  "Dashboard.html", 
                  { "all_product": all_product,
                    "filter1": Product1.objects.all(),
                    "categories": Category.objects.all(),
                    "filter2": filter2,
                    "ProductStock":ProductStock,
                    "total_product_count":total_product_count,
                    "products": products,
                    "categories":categories, 
                
                                         
                                     
                 })  # ✅ ควรไม่มี `redirect()` ตรงนี้


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



@method_decorator(csrf_exempt, name="dispatch")
class UpdateStockAPIView(APIView):
    permission_classes = [AllowAny]  # ✅ ปิดการตรวจสอบสิทธิ์ (ใช้ AllowAny แทนได้)

    def put(self, request, *args, **kwargs):
        updates = request.data.get("updates", [])

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
    
    

@ensure_csrf_cookie  # ✅ บังคับให้เซิร์ฟเวอร์ตั้งค่า CSRF Token
def my_view(request):
    return JsonResponse({"message": "CSRF Token set"})
    
@method_decorator(csrf_exempt, name='dispatch')  # ✅ ปิด CSRF Protection เฉพาะ API นี้
class SaveSaleRecordAPIView(APIView):
    
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]  # ✅ ใช้ CsrfExemptSessionAuthentication
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

    
            
        
        


def calculate_crc16(data: str) -> str:
    """
    คำนวณค่า CRC16 ตามมาตรฐาน CCITT-FALSE
    :param data: ข้อมูลในรูปแบบ string
    :return: ค่า CRC16 ในรูปแบบ hexadecimal
    """
    poly = 0x1021
    crc = 0xFFFF

    for byte in data.encode('utf-8'):
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFFFF  # ให้ค่าอยู่ในขอบเขต 16-bit

    return f"{crc:04X}"  # คืนค่าในรูปแบบ hexadecimal 4 หลัก

def generate_promptpay_qr(request):
    phone_number = request.GET.get('phone_number')  # รับหมายเลขโทรศัพท์
    amount = request.GET.get('amount')  # รับจำนวนเงิน

    if not phone_number or not amount:
        return JsonResponse({"error": "Missing phone_number or amount."}, status=400)

    try:
        # ตรวจสอบรูปแบบหมายเลขโทรศัพท์ (เพิ่มรหัสประเทศไทย 66)
        if phone_number.startswith("0"):
            phone_number = "66" + phone_number[1:]

        # สร้าง QR Content ตามมาตรฐาน PromptPay
        payload_format_indicator = "000201"
        point_of_initiation_method = "010211"
        merchant_account_info_template = "2937"
        promptpay_id = f"0016A000000677010111011300{phone_number}"
        country_code = "5802TH"
        transaction_currency = "5303764"
        transaction_amount = f"5406{float(amount):06.2f}"
        checksum_tag = "6304"
        Add_amount="FCA2"

        # Assemble the full data string before checksum
        qr_content = (
            payload_format_indicator +
            point_of_initiation_method +
            merchant_account_info_template +
            promptpay_id +
            country_code +
            transaction_currency +
            transaction_amount +
            checksum_tag+
            Add_amount
        )

        # คำนวณ CRC16
        crc_value = calculate_crc16(qr_content[:-4])  # Exclude placeholder checksum
        final_qr_content = qr_content[:-4] + crc_value

        # Debug: แสดง QR Content และ CRC16
        print("Final QR Content:", final_qr_content)

        # สร้าง QR Code
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(final_qr_content)
        qr.make(fit=True)

        # แปลง QR Code เป็น base64
        buffer = io.BytesIO()
        img = qr.make_image(fill_color="black", back_color="white")  # สร้างรูปภาพจาก QR Code
        img.save(buffer, format="PNG")  # บันทึก QR Code ลงใน buffer
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()

        return JsonResponse({"qr_code": qr_code_base64, "content": final_qr_content})

    except ValueError:
        return JsonResponse({"error": "Invalid amount."}, status=400)

def CleanDisplay(request):
    
   return render (request,"Dashboard.html")