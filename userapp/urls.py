from django.urls import path
from userapp import views

urlpatterns = [


path('product/register', views.register, name='register.html'),
path('product/login', views.login, name='login.html'),
path('product/logout', views.logout, name='logout.html'),

path('register', views.register, name='register.html'),
path('login',views.login, name='login.html'),
path('logout', views.logout, name='logout.html'),
    
]
