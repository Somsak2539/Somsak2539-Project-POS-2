




from django.urls import path
from productapp import views
from .views import search_products # สำหรับการimport view สำหรับการค้นหา
from rest_framework.routers import DefaultRouter #เป็นของคำสั่ง View Reset


from django.conf import settings
from django.conf.urls.static import static

#register
urlpatterns = [

    path("layoutNew",views.layoutNew),
    path("indexNew",views.indexUpdate,name="indexNew"),
    path("search/", search_products, name="search_products"), 
   
    path("ProductNew",views.ProductNew,name="Productnew"),
    path("",views.index),
    path('product/<int:id>/', views.productDetail, name='productDetail'), #การเรียกใช้ blog ตามด้วย id
    path('product/',views.product_list,name='product1'),
    path('list/', views.BlogList.as_view()),              #ทำการแปลง class ให้เป็น function  (* ถ้าเป็นรูปแบบ function based ไม่จำเป็นต้องเติม .as.view() เข้าไปในนั้น * )
    path('detail/<int:id>/',views.BlogDetail.as_view())   #ทำการแปลง class ให้เป็น function (* ถ้าเป็นรูปแบบ function based ไม่จำเป็นต้องเติม .as.view() เข้าไปในนั้น * )
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   
