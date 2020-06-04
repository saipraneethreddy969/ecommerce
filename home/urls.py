from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('signin/',views.signin),
    path('register/',views.register),
    path('logout/',views.logout),
    path('base/',views.base),
    path('apparels/',views.apparels),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('add_cart/',views.add_cart),
]  