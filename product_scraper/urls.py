from django.urls import path, include
from product_scraper import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('product/<int:pk>/', views.ProductId.as_view()),
]
