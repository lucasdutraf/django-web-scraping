from django.urls import path, include
from product_scraper import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.ItemsList.as_view()),
    path('product/<int:pk>/', views.ItemId.as_view()),
]
