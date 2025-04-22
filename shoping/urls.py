"""
URL configuration for shoping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static  #ใน Django เพื่อใช้สำหรับการให้บริการไฟล์สื่อ (media files) ในโหมด development
from django.conf import settings  #ป็นการนำเข้า (import) ตัวแปร settings จากโมดูล django.conf ใน Django ซึ่งเป็นตัวแปรที่ให้คุณเข้าถึงการตั้งค่า (configuration) ของโปรเจกต์ Django ที่กำหนดไว้ในไฟล์ settings.py
from rest_framework.routers import DefaultRouter #เป็นของคำสั่ง View Reset
from .custom_admin import custom_admin  # ✅ นำเข้า Custom Admi # ✅ นำเข้า Custom Admin
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()

admin.site.site_header="somsak sonngai"
admin.site.site_title="somsak sonngai"
admin.site.index_title="somsak sonngai"


# ปิด CSRF เฉพาะที่ admin ทำการปิด CSRF 
#admin.site.login = csrf_exempt(admin.site.login)

urlpatterns = [
   
    path('admin/', admin.site.urls,name='admin1'),
    path('',include("DashboardUser.urls")),
    path('',include("productapp.urls")),
    path('', include('chat.urls')),
    path('',include("userapp.urls")),
    path('',include("cartapp.urls")),
    path('',include("orderapp.urls")),
    path('',include("Dashboard.urls")), ##ทำงานในส่วนนี้ก่อนฃ
    path('',include(router.urls)) , # สำหรับการติดตั้ง rounter
    path('api/',include("productapp.urls")), #เป็นการเพิ่ม path สำหรับการอ้างอิงในโปรเจค ต้องไปตามที่  blogApp urls ว่ามอะไรบ้าง และurls ได้ทำการกำหนดอะไรบ้างใน urls นี้ก็คืออีกหนั่งอย่างสำหรับการตามหาที่อยู่ Urls โค้ดสำคัญเลยแหละ
    path('blog/',include("productapp.urls")),
    
   
    
   
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #เป็นคำสั่งที่ใช้เพิ่มเส้นทาง (URL pattern) สำหรับให้บริการไฟล์สื่อ (media files) ในโหมด development ของ Django โดยการเชื่อมโยง MEDIA_URL กับ MEDIA_ROOT เพื่อให้ Django สามารถให้บริการไฟล์สื่อผ่านเว็บเซิร์ฟเวอร์ได้