from django.shortcuts import render
from django.urls import path,include
from DashboardUser import views
from .views import Circulation2 


# Create your views here.
urlpatterns = [

path("indexDashboardUser/",views.Circulation2,name="indexDashboardUser"),
path("index",views.index,name="index"), #1
path("LayoutDashbords",views.LayoutDashbords,name="LayoutDashbords"),
path("LayoutDashbords1",views.LayoutDashbords1,name="LayoutDashbords1"),
path ("Calender",views.Calender, name="Calender"),
path ("ItemProduct",views.ItemProduct, name="ItemProduct"), #2
path ("Circulation",views.Circulation1, name="Circulation1"), #3
path ("Circulation1",views.Circulation3, name="Circulation3"), 
path ("Circulation3",views.check_time, name="Circulation4"), 
path ("ProductPreview/",views.ProductPreview, name="ProductPreview"), #4
path("EditAdd/<int:id>/",views.EditAdd, name="EditAdd"),#5
path("login_cover/",views.login_cover, name="login_cover"),
path('logout_cover', views.logout_cover, name='logout_cover'),
path('eror404/', views.eror404, name='eror404'),
path('apps_ecommerceCart/', views.apps_ecommerceCart, name='apps_ecommerceCart'),
path("apps-ecommerceCartAjax/",views.apps_ecommerceCartAjax,name="apps-ecommerceCartAjax"),
path('products/<int:pk>/update-price-stock/', views.update_product_price_stock, name='update_product_price_stock'),
path('app_add_product/', views.apps_add_product, name='apps_add_product'),
path('app_invoiceAdd/', views.invoiceAdd, name='app_invoiceAdd'),
path('apps-invoiceList/', views.appsinvoiceList, name='apps-invoiceList'),
path('admin/ajax/load-products/', views.load_products, name='ajax_load_products'),
path('select2/', include('django_select2.urls')),



path('Sellers/', views.Sellers, name='Sellers'),  # สำหรับกรณีที่ไม่มี seller_id (สร้าง seller ใหม่)
path('Sellers/<int:seller_id>/', views.Sellers, name='seller_edit'),  # สำหรับการแก้ไขข้อมูล
path('Sellers/<int:seller_id>/delete/', views.seller_delete, name='seller_delete'),
path('Customers/', views.Customers, name='Customers'),
path('customers/', views.Customers, name='Customers'),
path('customers/add/', views.add_customer, name='add_customer'),
path('customers/<int:customer_id>/edit/', views.customer_edit, name='customer_edit'),
path('customers/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
path('invoiceList/', views.invoicelist, name='invoiceList'),
path('Drafducument/', views.Drafducument, name='Drafducument'),
path('recriptAdd/', views.recriptAdd, name='recriptAdd'),
path('recriptRecord/', views.recriptRecord, name='recriptRecord'),
path('add-invoice/', views.add_invoice, name='add_invoice'),
path('save_invoice/', views.save_invoice, name='save_invoice'),

]