from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, DataError
from .models import Product
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request,'products/home.html', {'products':products})

@login_required(login_url='/login/')
def create_product(request):
    if request.method == "POST":
        product = Product()
        product.title = request.POST['title']
        product.url = request.POST['url']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.body = request.POST['body']
        product.hunter = request.user
        try:
            product.save()
            return redirect('detail', product.id)
        except DataError:
            return render(request,'products/createproduct.html', {'error':'Invalid Data Entered'})
    else:
        return render(request,'products/createproduct.html')

def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'products/productdetail.html', {'product': product})


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request,user)
                return redirect('/')
            except IntegrityError:
                return render(request,'products/signup.html', {'error':'Uesrname already exixts'})
        else:
            return render(request,'products/signup.html', {'error':'Passwords did not match'})
    else:
        return render(request,'products/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'products/login.html', {'error':'Incorrect Username or Password'})
    else:
        return render(request,'products/login.html')

def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
