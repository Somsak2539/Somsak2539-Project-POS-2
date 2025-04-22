from django.urls import path
from Dashboard import views
from .views import UpdateStockAPIView,SaveSaleRecordAPIView,CleanDisplay

from django.urls import path
from .views import generate_promptpay_qr
from .views import check_auth


urlpatterns = [

  path ('Dashboard/',views.ShowDashBoard,name="Dashboard"),
  path("update-stock/",UpdateStockAPIView.as_view(), name="update_stock"),
  path('save-sale-record/',SaveSaleRecordAPIView.as_view(), name='save_sale_record'),
  path('generate-promptpay-qr/', generate_promptpay_qr, name='generate_promptpay_qr'),
  path ('login_cover/?next=/indexDashboardUser//',views.CleanDisplay),
  path('check-auth/', check_auth, name='check_auth'),
  path('Recipe',views.Recipe, name='Recipe'),
  path('ShowForDisplay',views.ShowForDisplay, name='ShowForDisplay'),
  path("get-product-list/", views.get_product_list, name="get_product_list"),
  path("product_list_ajax/",views.product_list_ajax,name="product_list_ajax"),
  path("my_view/",views.my_view,name="my_view"),
  
  
  
]