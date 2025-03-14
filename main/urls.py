# URLS MAIN

from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('category-list/', views.category_list,name='category_list'),
    path('marca-list/', views.marca_list,name='marca_list'),
    path('product-list/', views.product_list,name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)