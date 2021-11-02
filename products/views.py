from django.shortcuts import render

def home(request):
    return render(request,'products/home.html')

def signup(request):
    return render(request,'products/signup.html')

def signin(request):
    return render(request,'products/login.html')
