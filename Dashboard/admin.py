from django.contrib import admin
from Dashboard.models import OrderSele
from .models import SaleRecord
from rangefilter.filters import DateRangeFilter
import openpyxl
from django.http import HttpResponse



# Register your models here.

#class ProfitSele(admin.ModelAdmin):
#    list_display=["product","price","quantity","created","customer","Pofitprice",]
      
#admin.site.register(OrderSele,ProfitSele)




class SaleRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_amount', 'entered_amount', 'change', 'timestamp', 'all_stock_adjustments','cashier']
    list_filter = [('timestamp', DateRangeFilter)]  # ใช้ DateRangeFilter
    actions_on_top = True  # แสดง Actions ด้านบน
    actions_on_bottom = True  # แสดง Actions ด้านล่าง
    actions = ["export_as_excel",]



    def all_stock_adjustments(self, obj):
        """แสดงรายการทั้งหมดใน stock_adjustments"""
        if obj.stock_adjustments is not None and isinstance(obj.stock_adjustments, list):
         # ดึงข้อมูลทั้งหมดจาก stock_adjustments และแปลงเป็นข้อความ
            return ", ".join(
                 [
                     f"สินค้า: {item.get('product', 'N/A')}, "
                     f"จำนวน: {item.get('quantity', 'N/A')} unit, "
                     f"กำไร: {float(item.get('totalProfit') or 0):.2f} บาท, "
                     f"รวมราคา: {float(item.get('TotalPrice') or 0):.2f} บาท"
                     for item in obj.stock_adjustments if isinstance(item, dict)
                 ]
             )
        return "No Data"



  
  
    all_stock_adjustments.short_description = "Stock Adjustments"






    def export_as_excel(self, request, queryset):
        
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Products"

            headers = ['id', 'total_amount', 'entered_amount', 'change', 'timestamp', 'all_stock_adjustments']
            sheet.append(headers)

            for obj in queryset:
                timestamp = obj.timestamp.replace(tzinfo=None) if obj.timestamp else None  # แก้ไขตรงนี้
                sheet.append([
                    obj.id,
                    obj.total_amount,
                    obj.entered_amount,
                    obj.change,
                    timestamp,
                    self.all_stock_adjustments(obj),
                ])

            response = HttpResponse(
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            response["Content-Disposition"] = 'attachment; filename="products.xlsx"'

            workbook.save(response)
            return response
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
    
    
    
    

admin.site.register(SaleRecord, SaleRecordAdmin)