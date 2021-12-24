"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
# from .views import Index

urlpatterns = [

    path('', views.index,name ="index"),
    path('login/',views.login ,name = "login"),
    path('signup/', views.signup,name = "signup"),
    path('logout/', views.logout,name = "logout"),
    path('account/', views.account,name = "account"),
    path('cart/', views.cart,name = "cart"),
    path('product_view/', views.product_view,name = "product_view"),
    path('about/', views.about,name = "about"),


]
