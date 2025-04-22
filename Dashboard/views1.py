from django.shortcuts import render,redirect
from productapp.models import Product1
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
import pytz
from django.utils.timezone import make_aware
from django.utils import timezone  # ✅ นำเข้า timezone สำหรับจัดการโซนเวลา
import time


# Create your views here.









def Recipe(request):
    
    return render(request,"Recipe.html")



@login_required
def check_auth(request):
    return JsonResponse({"authenticated": True, "user": request.user.username})



def is_special_admin(user):
    return user.is_authenticated and user.groups.filter(name='Dashboards').exists()





@login_required(login_url='/login_cover/')
@user_passes_test(is_special_admin)
def ShowDashBoard(request): 
    # ✅ ดึง SaleRecord ทั้งหมดเรียงตาม timestamp ล่าสุด
    ShowRecord = SaleRecord.objects.all().order_by("-timestamp")

    # ✅ ดึง SaleRecord ล่าสุด (ถ้ามี)
    latest_record = ShowRecord.first()

    # ✅ ตรวจสอบว่ามีข้อมูลหรือไม่
    if latest_record:
        bangkok_tz = pytz.timezone("Asia/Bangkok")
        timestamp_th = latest_record.timestamp.astimezone(bangkok_tz)
    else:
        timestamp_th = None

    # ✅ Debug ค่าที่ดึงมา
    print("✅ [DEBUG] Sale Records:", ShowRecord)
    print(f"✅ [DEBUG] Sale Record ล่าสุด: {latest_record}")
    print(f"✅ [DEBUG] Timestamp (TH): {timestamp_th if timestamp_th else 'ไม่มีข้อมูล'}")

    return render(request, "Dashboard.html", {
        "ShowRecord": ShowRecord,
        "latest_record": latest_record,
        "timestamp_th": timestamp_th
    })

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
    
    
    
class SaveSaleRecordAPIView(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]  # ✅ รองรับการใช้ session
    permission_classes = [IsAuthenticated]  # ✅ บังคับให้ต้องล็อกอิน
    def post(self, request):
        try:
            data = request.data
            
           
           
            #✅ ตรวจสอบว่า stock_adjustments เป็น JSON หรือไม่
            stock_adjustments = data.get("stockAdjustments")
            if isinstance(stock_adjustments, str):
                try:
                    stock_adjustments = json.loads(stock_adjustments)
                except json.JSONDecodeError:
                    return Response({"error": "Invalid JSON format for stock_adjustments"}, status=status.HTTP_400_BAD_REQUEST)
    
    
             # ✅ แปลงเวลาให้เป็นโซนไทย (Asia/Bangkok)
          
            SaleRecord.objects.create(
                total_amount=data["totalAmount"],
                entered_amount=data["enteredAmount"],
                change=data["change"],
                timestamp=datetime.fromisoformat(data["timestamp"]),
                stock_adjustments=data["stockAdjustments"],
                cashier=request.user,
               
                
            )
            
            
            time.sleep(1)  # ✅ หน่วงเวลาให้ Database Sync
            return Response({"message": "Sale record saved successfully!"}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({"error": f"Missing key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
            
        
        
        
@method_decorator(csrf_exempt, name='dispatch')
class DashboardAPIView(APIView):
    def put(self, request):
        return Response({"message": "Success!"}, status=200)     


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