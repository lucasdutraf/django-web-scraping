from django.shortcuts import render
from rest_framework import generics
from .db_helper import populate_product_db
from .serializers import ProductSerializer
from .models import Product

class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductId(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer