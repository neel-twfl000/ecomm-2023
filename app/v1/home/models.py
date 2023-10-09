from django.db import models
from django.db.models import F, Q, Subquery, Exists, OuterRef
from django.db.models.query import QuerySet
from base.models import Account, BaseModel
from django.utils.text import slugify
from base.choices import Choices
# Create your models here.

### QUERY SET ###
class ProductQuerySet(models.QuerySet):
    def shop_product(self):
        return self.filter(
            ~Q(Exists(DealsOffer.objects.filter(product_list__id=OuterRef('pk'), is_active=True))),
            is_active=True
            ).annotate(
            discount_rate = ((F('price')-F('discount_price'))*100)/F('price'),
            purchase_price=F('gst_price')+F('discount_price'),
            ).order_by('-created_at')
    
    def all(self):
        return self.filter(
            is_active=True
            ).annotate(
            discount_rate = ((F('price')-F('discount_price'))*100)/F('price'),
            purchase_price=F('gst_price')+F('discount_price'),
            ).order_by('-created_at')

### MANAGER ###
# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model, using=self._db)
    
#     def shop_product(self):
#         return self.get_queryset().shop_product()



### MODELS ###
class Banner(BaseModel):
    banner_type = models.IntegerField(choices=Choices().banner_type, default=1, unique=True)
    header = models.CharField(max_length=130)
    text_1 = models.CharField(max_length=130)
    text_2 = models.CharField(max_length=130)
    image = models.ImageField(null=True, blank=True, upload_to='banner/')
    shop_url = models.URLField(null=True, blank=True)
    pass

    def __str__(self) -> str:
        return f"{self.header} ({self.banner_type})"

class Category(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        unique_together = ('category', 'name',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.category.name} -- {self.name}"

class Brand(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=130)
    slug = models.SlugField(max_length=130, blank=True, null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    back_image = models.ImageField(null=True, blank=True)
    price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    gst_price = models.FloatField(default=0)
    description = models.TextField(null=True)
    objects = ProductQuerySet.as_manager()

    class Meta:
        unique_together = ('category', 'name', 'brand')

    def __str__(self) :
        return self.name 
    
    def save(self, *args, **kwargs):
        self.gst_price = (self.discount_price*self.gst)/100
        if not self.id:
            super(Product, self).save(*args, **kwargs)
            self.slug = f"{slugify(self.name)}-{self.id}"
            super(Product, self).save(*args, **kwargs)
        else:
            self.slug = f"{slugify(self.name)}-{self.id}"
            super(Product, self).save(*args, **kwargs)


    # @property
    # def purchase_price(self):
    #     return self.gst_price+self.discount_price

    # @property
    # def discount_rate(self):
    #     off_rate = self.price-self.discount_price
    #     return (off_rate*100)/self.price

    # @property
    # def varient(self):
    #     return ProductVarient.objects.filter(product=self)

    # @property
    # def varient_type_list(self):
    #     return MyChoice().varient_type

    # @property
    # def get_status(self):
    #     data = MyChoice().product_status
    #     for i in data:
    #         if self.status == i[0]:
    #             return i[1]
                
    #     return self.ac_type


class DealsOffer(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True, blank=True, null=True)
    product_list = models.ManyToManyField(Product)
    off_rate = models.FloatField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.name)}"
        super(DealsOffer, self).save(*args, **kwargs)
        return self
    
    def __str__(self) :
        return self.name 



# class ProductVarient(BaseModel):
#     pass

# class color(BaseModel):
#     pass

# class ProductAvailability(BaseModel):
#     pass

