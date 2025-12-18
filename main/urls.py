from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='Home'),
    path('products/', views.Products,name='Products'),
    path('about/', views.About,name='About'),
    path('contact/', views.Contact,name='Contact'),
    path('register/', views.register,name='register'),
    path('verify_otp/', views.verify_otp,name='verify_otp'),
]
