from django.contrib import admin
from productapp.models import Product, Product1, Category,frolink
from django.db.models import Sum
from django.utils.html import format_html
import openpyxl
from django.http import HttpResponse
from django.forms import TextInput
from django.db import models



from django.urls import path, reverse


     
'''class ManageProduct(admin.ModelAdmin):
    list_display = ["name", "price", "is_trending", "stock", "image"]

admin.site.register(Product, ManageProduct)'''

class ManageProduct1(admin.ModelAdmin):
    list_display = ["id","name"]

admin.site.register(Category, ManageProduct1)


class CategoryListFilter(admin.SimpleListFilter): # สร้าง class ให้เรียงตามตัวอักษรภาษาไทยและภาษา 
    title = 'ประเภทรายการ'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        # ดึงชื่อหมวดหมู่ทั้งหมดแล้วเรียงตามชื่อ
        categories = Category.objects.order_by('name')  # เปลี่ยน 'name' ให้ตรงกับ field ที่ใช้ใน Category
        return [(cat.id, cat.name) for cat in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset
    

class ManageProduct2(admin.ModelAdmin):
    
    list_display = ["id","image_preview","name","stock","price","profitprice","barcode","is_trending",]
    list_editable = [ "is_trending", "stock","profitprice","price"]
    list_per_page = 20  # แสดงข้อมูล 20 รายการต่อหน้า
    search_fields = ["name","barcode","id"]  # เพิ่มช่องค้นหา
    list_filter = [CategoryListFilter]  # เปลี่ยนจาก "category" เป็น filter ที่เราสร้างเอง  # เพิ่มตัวกรองตามหมวดหมู่ 
    actions_on_top = True  # แสดง Actions ด้านบน
    actions_on_bottom = True  # แสดง Actions ด้านล่าง
    actions = ["export_as_csv", "export_as_excel", "mark_as_trending", "mark_as_not_trending"]
    
   
    class Media:
        js = [
        "https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js",  # ระบุเวอร์ชันชัดเจน
        "js/barcode_scanner_v22.js",  # ไฟล์ของเราต้องแน่ใจว่า static โหลดได้จริง 427035
    ]


    
  

    def profit_margin(self, obj):
        return obj.price - obj.profitprice
    profit_margin.short_description = "Profit Margin"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "แสดงรูปภาพ"

    def export_as_excel(self, request, queryset):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Products"

        headers = ["ID", "Name", "Price", "Stock", "Profit Price", "Barcode"]
        sheet.append(headers)

        for obj in queryset:
            sheet.append([obj.id, obj.name, obj.price, obj.stock, obj.profitprice, obj.barcode])

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="products.xlsx"'

        workbook.save(response)  # บันทึกไฟล์ลง Response
        return response

   


    def changelist_view(self, request, extra_context=None):
        # ดึง queryset ที่กรองในหน้า Admin
        queryset = self.get_queryset(request)
        # คำนวณ Total Price ของสินค้าทั้งหมด
        total_price = queryset.aggregate(Sum('price'))['price__sum'] or 0
        # ส่งข้อมูลไปยัง context
        extra_context = extra_context or {}
        extra_context['total_price'] = total_price
        return super().changelist_view(request, extra_context=extra_context)
    


admin.site.register(Product1, ManageProduct2)



class link(admin.ModelAdmin):
    list_display = ('name','url_link')

    def url_link(self, obj):
        url = reverse('indexDashboardUser')  # ใช้ชื่อ URL ที่กำหนดใน urls.py
        return format_html('<a href="{}" target="">{}</a>', url, obj.name)
    url_link.short_description = 'Product Link'

admin.site.register(frolink, link)

















