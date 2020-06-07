"""ecomsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('signin/',include('home.urls')),
     path('register/',include('home.urls')),
     path('base/',include('home.urls')),
     path('apparels/',include('home.urls'),name="apparels"),
     path('cart/',include('home.urls')),
     path('add_cart/',include('home.urls')),
     path('checkout/',include('home.urls'),name="checkouts"),
     path('process_order/',include('home.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
