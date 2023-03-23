"""trp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from trp_db.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('auth/', auth),
    path('reg/', reg),
    path('search/', search),
    path('orders/',orders),
    path('spareparts', spareparts),
    path('order_card/<ID_CommNumber>', order_card),
    path('prod_card/<id_num>', prod_card),
    path('logout/', logout_user),
    path('test/', test)
]
