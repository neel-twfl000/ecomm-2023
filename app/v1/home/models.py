from django.db import models
from base.models import Account, BaseModel
from django.utils.text import slugify
# Create your models here.

# class DealsOffer(BaseModel):

# class Banner(BaseModel):
#     name = models.CharField(max_length=30)
#     image = models.ImageField(null=True, blank=True)
#     shop_url = models.URLField()

#     pass

# class Category(BaseModel):
#     name = models.CharField(max_length=30, unique=True)
#     name_slug = models.SlugField(max_length=30, unique=True, blank=True, null=True)
#     cover_image = models.ImageField(null=True, blank=True)
#     pass

#     def save(self, *args, **kwargs):
#         self.name_slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)

# class SubCategory(BaseModel):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=30, unique=True)
#     name_slug = models.SlugField(max_length=30, unique=True, blank=True, null=True)
#     cover_image = models.ImageField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         self.name_slug = slugify(self.name)
#         super(SubCategory, self).save(*args, **kwargs)

# class Brand(BaseModel):
#     name = models.CharField(max_length=30, unique=True)
#     name_slug = models.SlugField(max_length=30, unique=True, blank=True, null=True)
#     cover_image = models.ImageField(null=True, blank=True)
    
#     def save(self, *args, **kwargs):
#         self.name_slug = slugify(self.name)
#         super(Brand, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

# class Product(BaseModel):
#     pass

# class ProductVarient(BaseModel):
#     pass

# class color(BaseModel):
#     pass

# class ProductAvailability(BaseModel):
#     pass

