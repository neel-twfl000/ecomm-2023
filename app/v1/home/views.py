from django.shortcuts import render, HttpResponse
from .models import Account
from .models import Banner, Brand, Category, Product, DealsOffer
from django.views import View
from django.db.models import F, Subquery
# Create your views here.
html_path = lambda page: f"home/pages/{page}.html"


class Home(View):

    def get(self, request):
        data = {"show_category":True}
        data['banner'] = Banner.objects.all().order_by('banner_type')
        data['brand'] = Brand.objects.all().order_by('-name')[0:15]
        data['category'] = Category.objects.all().prefetch_related('subcategory_set')
        data['product'] = Product.objects.shop_product()[0:10]
        data['deals'] = []
        for i in DealsOffer.objects.filter(is_active=True)[0:3]:
            obj = {"id":i.id, "name":i.name, "slug":i.slug}
            obj["products"] = i.product_list.all().annotate(
                before_price = F('discount_price') + (F('discount_price')*F('gst')/100),
                deal_off_price = F('discount_price')-(F('discount_price')*i.off_rate)/100,
                gst_price = (F('deal_off_price')*F('gst'))/100,
                purchase_price = F('deal_off_price')+F('gst_price'),
                discount_rate = ((F('discount_price')-F('deal_off_price'))*100)/F('discount_price'),
            )
            data['deals'].append(obj)
        
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
