from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

class CustomAdminSite(AdminSite):
    site_header = _("ระบบจัดการเว็บไซต์")  # เปลี่ยนชื่อหัวข้อด้านบน
    site_title = _("แผงควบคุมระบบ")  # เปลี่ยนชื่อของ Title Tab
    index_title = _("จัดการบัญชีผู้ใช้")  # ✅ เปลี่ยนชื่อ Authentication and Authorization

# ✅ สร้าง Custom Admin
custom_admin = CustomAdminSite(name="custom_admin")

# ✅ นำ Users และ Groups ไปใส่ใน Custom Admin
custom_admin.register(User, admin.ModelAdmin)
custom_admin.register(Group, admin.ModelAdmin)
