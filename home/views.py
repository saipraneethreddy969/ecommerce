from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Products
def base(request):
    return render(request,'base.html')

def apparels(request):

    products=Products.objects.all()
    context={
        'product':products
    }

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
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')

    