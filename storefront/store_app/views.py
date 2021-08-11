from django.shortcuts import render
from .models import *

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request,'shop.html', context)
