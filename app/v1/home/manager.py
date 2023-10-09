from django.db import models
from django.db.models import F, Q, Subquery, Exists

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True
            ).annotate(
            discount_rate = ((F('price')-F('discount_price'))*100)/F('price'),
            purchase_price=F('gst_price')+F('discount_price'),
        ).order_by('-created_at')