
from django.urls import path
from cartapp import views


urlpatterns = [

  path ('cart',views.cart, name='cart')
, path ('cart/add/<int:product_id>',views.addCart,name="addCart"),
  path('cart/remove/<int:product_id>',views.removeCart,name="removeCart")


]