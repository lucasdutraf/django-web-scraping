from django.shortcuts import render
from rest_framework import generics
from .db_helper import populate_product_db
from django.http import HttpResponse, JsonResponse
import os


def get_all_products(request):
    response = populate_product_db()
    return JsonResponse(response, safe=False)