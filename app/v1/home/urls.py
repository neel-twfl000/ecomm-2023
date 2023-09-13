from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home),
    path('category/', views.category_product),
    path('product/', views.product),
    path('cart/', views.cart),
    path('wishlist/', views.wishlist),
    path('checkout/', views.checkout),
]