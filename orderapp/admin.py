from django.contrib import admin
from orderapp.models import Order,OrderDetail
# Register your models here.



'''class ManageProduct3(admin.ModelAdmin):
    
    list_display = ["fullname", "phone","address","total_with_comma", "created","customer"]
    
admin.site.register(Order, ManageProduct3)



class ManageProduct4(admin.ModelAdmin):
    
    list_display = ["product","price_with_comma","quantity","created","order","sub_total","DetailBuy"]
    
admin.site.register(OrderDetail, ManageProduct4)'''

