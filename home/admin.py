from django.contrib import admin
from .models import Products,customer,Order,orderitem,shippingAddress

admin.site.register(Products)
admin.site.register(customer)
admin.site.register(shippingAddress)
admin.site.register(Order)
admin.site.register(orderitem)
