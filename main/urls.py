from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='Home'),
    path('products/', views.Products,name='Products'),
    path('about/', views.About,name='About'),
    path('contact', views.Contact,name='Contact'),
]
