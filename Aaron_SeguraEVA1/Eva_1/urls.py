"""
URL configuration for Eva_1 project.

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
from django.urls import path
from Eva_1App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('web/', views.renderTemplate),
    path('alimentos/', views.alimentos,name='alimentos'),
    path('alimentos/alimento1/',views.alimento1),
    path('alimentos/alimento2/',views.alimento2),
    path('alimentos/alimento3/',views.alimento3),
    path('bebidas/',views.bebidas,name='bebidas'),
    path('bebidas/bebida1/',views.bebida1),
    path('bebidas/bebida2/',views.bebida2),
    path('bebidas/bebida3/',views.bebida3),
    path('postres/',views.postres,name='postres'),
    path('postres/postre1/',views.postre1),
    path('postres/postre2/',views.postre2),
    path('postres/postre3/',views.postre3),
    path('volver/<str:url_destino>/', views.volver_atras,name='volver_atras'),
    ]