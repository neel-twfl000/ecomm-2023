from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('db/', admin.site.urls),
    path('', include('v1.home.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
