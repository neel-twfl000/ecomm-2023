from django.urls import path, include
from .import views

app_name="home"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('category/', views.category_product),
    path('product/', views.product),
    path('cart/', views.cart),
    path('wishlist/', views.wishlist),
    path('checkout/', views.checkout),
]