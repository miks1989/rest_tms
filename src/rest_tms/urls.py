
from django.contrib import admin
from django.urls import path, include

from rest_tms.views import Products

# from rest_tms.views import products, get_product_detail

from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', Products, basename='boris')

print(router.urls)

urlpatterns = [
    # path('', Products.as_view({'get': 'list', 'post': 'create'})),
    # path('<int:pk>/', Products.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', include(router.urls)),
    path('auth-drf/', include('rest_framework.urls')),

]
