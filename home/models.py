from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    opencart=models.BooleanField()
    transaction_id=models.CharField(max_length=200)
    date_ordered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class orderitem(models.Model):
    quantity=models.IntegerField(default=0)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)

class shippingAddress(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.address