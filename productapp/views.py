
from django.shortcuts import render,redirect

from productapp.models import Product1 #ทำการดึกข้อมูลจาก folder product ของไฟค์ models แล้วดึงข้อมูล product 1 เข้ามาทำงาน 
from django.core.paginator import Paginator #เป็นการกำหนดหน้าให้กลับหน้าเพจที่ html เพื่อทำการดึงข้อมูลจาก django 
from rest_framework.views import APIView # เอาไว้สำหรับการเรียกใช้ class Based Views 
from productapp.serializers import BlogSerializer,CategotySerializer
from django.http import JsonResponse #ดึงฟั่งชั่นจาก Django เพื่อใช้fucntion ของmyjason มาจาก Class based View เพื่อที่จะทำการนำมาใช้
from rest_framework.response import Response #มาจาก Class based View เพื่อที่จะทำการนำมาใช้
from rest_framework import status # คือการ impport แจ้งข้อมูล status สำหรับการทำผิดfuntion ที่ใข้งานมาจาก Class based View เพื่อที่จะทำการนำมาใช้
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.db import models
# Create your views here.


#----------------------------------------------------------------สำหรับการดึง laout ใหม่------------------------------

def ProductNew(request):
    
     all_product=Product1.objects.all().order_by("category") # เรียกลำดับจากชื่อสินค้า ถ้าเป็นการเพิ่ม order_by ตัวนี้จะมีการเชื่อมโยงกับ Product.html
     #กำหนดหมายเลขหน้า
     page=request.GET.get("page") # ดึงค่า parameter page เพิ่อระบุว่าผู้ใช้ต้องการดูหน้าที่เท่าไหร่ ถ้าไม่มี parametre page ใน url ค่านี้จะเป็น  None
     paginator=Paginator(all_product,20) #สร้าง object Paginator เพื่อแบ่งข้อมูล all_product ออกเป็นหน้า page โดยแต่ล่ะหน้าจะแสดงข้อมูล 3 รายการ
     all_product=paginator.get_page(page) #ดึงข้อมูลของหน้าที่ผู้ชายที่จะต้องการดู (ตามค่า page ที่ได้จาก url ) ถ้า page เป็น None  หรือไม่ถูกต้อง (เช่น มากกว่าจำนวณหน้าทั้งหมด ) จะดึงข้อมูลหน้าแรกมาให้โดยอัตโนมัติ
     return render (request,"ProductUpdate.html",{"all_product":all_product}) #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป




# ใน productapp/models.py



@receiver(post_delete, sender=Product1)
def delete_product_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


def search_products(request):
    query = request.GET.get("q", "").strip()  # ลบช่องว่างใน query
    
    

    if query:
        products = Product1.objects.filter(name__icontains=query).values("id", "name", "price", "image")
        products_list = list(products)

        for product in products_list:
            # สร้าง URL แบบเต็ม
            product["image"] = request.build_absolute_uri(f"/media/{product['image']}")

        return JsonResponse(products_list, safe=False)
    return JsonResponse([], safe=False)



def layoutNew(request):
    
   return render(request,"layoutUpdate.html")

def indexUpdate(request):
    filter1 = Product1.objects.all()
    Products = Product1.objects.filter(is_trending=True)  # ดึงสินค้าที่เป็นสินค้ายอดนิยม
    return render(request, "indexUpdate.html", {"Products": Products, "filter1": filter1})

  


def index(request): 
    Products=Product1.objects.filter(is_trending=True) #ดึงตัวแปรที่เป็นproduct1 และกรองเอาตัวที่เป็น จริง true หรือสินค้ายอดนิยมตัวนี้จะมีการอ้างอิงผ่าน index.html
    return render(request,"index.html",{"Products":Products}) #ดึงค่าตัวแปรเพื่อทำการวนลูป


def productDetail(request,id):
    product=Product1.objects.get(pk=id)
    return render (request,"detail.html",{"product":product}) #มันก็คือ Product1 นั้นแหละที่เรียกใช้ที่เก็บไว้ในตัวแปร product ถ้าต้องการที่จะทำการเรียกใช้ก็เรียกใช้ product
  
  
def product_list(request):
    
     all_product=Product1.objects.all().order_by("category") # เรียกลำดับจากชื่อสินค้า ถ้าเป็นการเพิ่ม order_by ตัวนี้จะมีการเชื่อมโยงกับ Product.html
     
     #กำหนดหมายเลขหน้า
     page=request.GET.get("page") # ดึงค่า parameter page เพิ่อระบุว่าผู้ใช้ต้องการดูหน้าที่เท่าไหร่ ถ้าไม่มี parametre page ใน url ค่านี้จะเป็น  None
     paginator=Paginator(all_product,10) #สร้าง object Paginator เพื่อแบ่งข้อมูล all_product ออกเป็นหน้า page โดยแต่ล่ะหน้าจะแสดงข้อมูล 3 รายการ
     all_product=paginator.get_page(page) #ดึงข้อมูลของหน้าที่ผู้ชายที่จะต้องการดู (ตามค่า page ที่ได้จาก url ) ถ้า page เป็น None  หรือไม่ถูกต้อง (เช่น มากกว่าจำนวณหน้าทั้งหมด ) จะดึงข้อมูลหน้าแรกมาให้โดยอัตโนมัติ
     return render (request,"product.html",{"all_product":all_product}) #ทำการดึงค่าตัวแปรมาเก็บไว้แล้ว Return กับไป


#--------------------------------------------------------class Based Views-API VIEW-----------------------------------------------------------------



class BlogList(APIView):
    def get(self,request):
        blogs=Product1.objects.all() #การดึง objectมาทั้งหมด
        serializer=BlogSerializer(blogs,many=True) # การแปลงข้อมูลให้เป็น Json
        return Response(serializer.data)
    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    
    
      
class  BlogDetail(APIView):

    def get(self,request,id):
        try:
            blog=Product1.objects.get(pk=id) #ประกาศเท่ากับ Blog เท่ากับ Blogเลือกตาม iD
            serializer=BlogSerializer(blog)
            return Response(serializer.data)
        except Product1.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,id):
        blog=Product1.objects.get(pk=id) #ประกาศเท่ากับ Blog เท่ากับ Blogเลือกตาม iD
        serializer=BlogSerializer(blog,data=request.data) #
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        blog=Product1.objects.get(pk=id) #ประกาศเท่ากับ Blog เท่ากับ Blogเลือกตาม iD
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    