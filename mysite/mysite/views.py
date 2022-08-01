from django.shortcuts import render
from store.models import Product
# Create your views here.

def home(request):
    produsts = Product.objects.all().filter(is_available = True)
    context = {
       'products': produsts
    }
    return render(request, 'home.html',context)