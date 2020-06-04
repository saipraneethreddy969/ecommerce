from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from .models import Products,customer,Order,orderitem
from django.http import JsonResponse
import json
def base(request):
    return render(request,'base.html')

def apparels(request):

    products=Products.objects.all()
    if(request.user.is_authenticated):
        customer_obj=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer_obj,opencart=True)
        items=order.orderitem_set.all()
        context={'items':items,'order':order,'product':products}
    else:
        items=[]
        order={'cart_items':0,'cart_total':0}
        context={'items':items,'order':order,'product':products}
    return render(request,'apparels.html',context)
    
def index(request):
    return render(request,'index.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def signin(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            context={'user':user}
            auth.login(request,user)
            return redirect('/',context)
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request,'signin.html')
def register(request):
    if(request.method=="POST"):
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email)
        if(user is not None):
            return redirect('/')
    else:
        return render(request,'register.html')


def cart(request):
    if(request.user.is_authenticated):
        customer_obj=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer_obj,opencart=True)
        items=order.orderitem_set.all()
        context={'items':items,'order':order}
    else:
        items=[]
        order={'cart_items':0,'cart_total':0}
        context={'items':items,'order':order}
    return render(request,'cart.html',context)


def checkout(request):
    return render(request,'checkout.html')

def add_cart(request):
    data=json.loads(request.body)  
    productid=data['productId']
    action=data['action']
    print(productid,action)
    product=Products.objects.get(id=productid)
    customer_obj=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer_obj,opencart=True)
    Orderitem,created=orderitem.objects.get_or_create(order=order,product=product)
    if(action=="add"):
        Orderitem.quantity=(Orderitem.quantity+1)
    elif(action=="remove"):
        Orderitem.quantity=(Orderitem.quantity-1)
    
    Orderitem.save()
    if(Orderitem.quantity<=0):
        Orderitem.delete()

    return JsonResponse("hello",safe=False)