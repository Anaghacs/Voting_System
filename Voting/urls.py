# This urls.py page is created by the developer.This urls pages denoted by the app pages and functions urls. 

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('signout',views.signout,name="signout"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('view_users',views.view_users,name="view_users"),
    path('approve/<int:id>/',views.approve,name="approve"),
    path('verified_users',views.verified_users,name="verified_users"),
    path('user_home',views.user_home,name="user_home")
]

