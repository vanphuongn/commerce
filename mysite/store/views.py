from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Q
from category.models import Category
from store.models import Product

# Create your views here.

def store(request, category_slug = None):
    if category_slug is not None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.all().filter(category = categories, is_available = True )
    else:
        products = Product.objects.all().filter(is_available = True).order_by('id')

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(products, 3)
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count

    }

    return render(request, 'store/store.html', context)


def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        products = Product.objects.order_by('-created_date').filter(
            Q(product_name__icontains=q) | Q(description__icontains=q))
        product_count = products.count()
    context = {
        'products': products,
        'q': q,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context=context)