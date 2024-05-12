from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Product
from django.urls import reverse_lazy


class MainPageView(ListView):
    template_name = 'catalog.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.all()
    
class CreateProductView(CreateView):
    modle = Product
    fields = '__all__'

    template_name = 'createProduct.html'
    success_url = reverse_lazy('main_page')

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all()
    