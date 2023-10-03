"""
URL configuration for Bbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Bapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('doner_reg',views.doner_reg,name='doner_reg'),
    path('buser_reg',views.buser_reg,name='buser_reg'),
    path('admin_log',views.admin_log,name='admin_log'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('log_out',views.log_out,name='log_out'),
    path('dele/<id>',views.dele,name='dele'),
  
]
