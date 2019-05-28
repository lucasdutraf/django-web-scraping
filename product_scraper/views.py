from django.shortcuts import render
from rest_framework import generics
from .db_helper import populate_product_db
from .serializers import ItemSerializer
from .models import Item

class ItemsList(generics.ListAPIView):
    queryset = Item.objects.all()    
    if not queryset:
        populate_product_db()
        queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemId(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer