from django.contrib import admin
from chat.models import Message
# Register your models here.

'''class Chatuser (admin.ModelAdmin):
    
    list_display = ("room", "username", "content", "timestamp")  # แสดงข้อมูลในหน้าแอดมิน
    list_filter = ("room", "username", "timestamp")  # สามารถกรองห้องแชทหรือผู้ใช้ได้
    search_fields = ("room", "username", "content")  # ค้นหาข้อความแชทได้

admin.site.register(Message,Chatuser)'''