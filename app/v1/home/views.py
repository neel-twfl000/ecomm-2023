from django.shortcuts import render, HttpResponse
# Create your views here.

html_path = lambda page: f"home/pages/{page}.html"

def home(request):
    data = {"show_category":True}
    return render(request, html_path('home'), data)

def category_product(request):
    return render(request, html_path('product_list'))

def product(request):
    return render(request, html_path('product_detail'))

def cart(request):
    return render(request, html_path('cart'))

def wishlist(request):
    return render(request, html_path('wishlist'))

def checkout(request):
    return render(request, html_path('checkout'))
