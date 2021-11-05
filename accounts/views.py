from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request,user)
                return redirect('/')
            except IntegrityError:
                return render(request,'accounts/signup.html', {'error':'Uesrname already exixts'})
        else:
            return render(request,'accounts/signup.html', {'error':'Passwords did not match'})
    else:
        return render(request,'accounts/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'accounts/login.html', {'error':'Incorrect Username or Password'})
    else:
        return render(request,'accounts/login.html')

def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
