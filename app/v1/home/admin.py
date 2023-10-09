from django.contrib import admin
from .models import (Banner, Brand, Category,
                     SubCategory, Product, DealsOffer)

all_model = (Banner, Brand, Category, SubCategory, Product, DealsOffer)
# Register your models here.
for i in all_model:
    admin.site.register(i)
