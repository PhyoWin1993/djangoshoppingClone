from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all()
    dict = {
        'title':'Home Page',
        'products':products
    }
    return render(request,'page/home.html',dict)

def about(request):
     return render(request,'page/about.html',{'title':'About Page'})