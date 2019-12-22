from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
import json
from django.core import serializers

def home(request):
    dict = {
        'title':'Product Home Page',
        'products':Product.objects.all()
    }
    return render(request,"product/home.html",dict)

def create(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            messages.success(request,'Product Created!')
            return redirect('product-home-page')

    else :
         form = ProductCreateForm()
    dict = {
        'title':'Product Home Page',
        'form':form
    }
    return render(request,"product/create.html",dict)

@staff_member_required
def edit(request,pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductCreateForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            messages.success(request,'Product Created!')
            return redirect('product-home-page')

    else :
         form = ProductCreateForm(instance=product)
    dict = {
        'title':'Product Home Page',
        'form':form
    }
    return render(request,"product/create.html",dict)

@login_required
def dele(request,name):
    object = Product.objects.filter(name=name)
    object.delete()
    messages.success(request,'Object Deleted!')
    return redirect('product-home-page')

def apiGetSingleProduct(request,id):
    product = Product.objects.filter(pk=id)
    j = serializers.serialize("json",product)
    return HttpResponse(j)

def apiGetMultipleProduct(request,str):
     singleList = str.split(",")
     listy = []
     for pd in singleList:
         pdAry = pd.split(":")
         itemId = pdAry[0]
         obj = Product.objects.filter(pk=itemId).first()
         listy.append(obj)

     j = serializers.serialize('json',listy)
     return HttpResponse(j)
