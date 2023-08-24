
from django.contrib import admin
from django.urls import path, include

from rest_tms.views import products, get_product_detail

urlpatterns = [
    path('', products),
    path('<int:pk>/', get_product_detail),

]
