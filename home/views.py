from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from .models import Products,customer,Order,orderitem,shippingAddress
from django.http import JsonResponse
import datetime
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
        print(user)
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
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        customer.objects.create(user=user,name=username,email=email)
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
    if(request.user.is_authenticated):
        customer_obj=request.user.customer
        shipping_add=shippingAddress.objects.filter(customer=customer_obj)
        order,created=Order.objects.get_or_create(customer=customer_obj,opencart=True)
        items=order.orderitem_set.all()
        context={'items':items,'order':order,'shipping_add':shipping_add}
    else:
        items=[]
        order={'cart_items':0,'cart_total':0}
        context={'items':items,'order':order,'shipping_add':[]}
    return render(request,'checkout.html',context)

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

def process_order(request):
    data=json.loads(request.body)
    transaction_id=datetime.datetime.now().timestamp()
    total=float(data['total'])
    if(request.user.is_authenticated):
        customer=request.user.customer;
        order=Order.objects.get(customer=customer,opencart=True);
        if(order.cart_total==total):
            order.opencart=False
            order.transaction_id=transaction_id
            order.save()
    shippingAddress.objects.create(
        customer=customer,
        order=order,
        state=data['shippinginfo']['state'],
        city=data['shippinginfo']['city'],
        zipcode=data['shippinginfo']['zipcode'],
        name=data['shippinginfo']['name'],
        address=data['shippinginfo']['address'],
    )
    return JsonResponse("hello",safe=False)