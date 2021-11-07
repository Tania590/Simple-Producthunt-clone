from django.shortcuts import render, redirect, get_object_or_404
from django.db import DataError
from .models import Product, Vote
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request,'products/home.html', {'products':products})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def upvote(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product,pk=pk)
        votes = Vote.objects.filter(voter__id=request.user.id, product__id=product.id)
        if votes.exists():
            return redirect('detail', product.id)
        else:
            vote = Vote()
            vote.product = product
            vote.voter = request.user
            vote.save()
            product.votes_total += 1
            product.save()
            return redirect('detail', product.id)
