"""
URL configuration for rodoban project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from core.views import index
from django.shortcuts import render
from cliente.models import Cliente
from vendedor.models import Vendedor
from fabricante.models import Fabricante
from . import views
from coleta.models import Coleta, PneusColeta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('',index, name='index'),
    path('clientes/', include('cliente.urls')),
    path('vendedores/', include('vendedor.urls')),
    path('fabricantes/', include('fabricante.urls')),
    path('tamanhos/', include('tamanho.urls')),
    path('produtos/', include('produto.urls')),
    path('coletas/', include('coleta.urls', namespace='coleta')),
]
