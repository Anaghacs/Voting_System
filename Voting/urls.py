# This urls.py page is created by the developer.This urls pages denoted by the app pages and functions urls. 

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('admin_home',views.admin_home,name="admin_home")
    
    
]
