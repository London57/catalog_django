from django.urls import path, include
from .views import MainPageView, CreateProductView

urlpatterns = [
    path('catalog/', MainPageView.as_view(), name='main_page'),
    path('catalog/create/', CreateProductView.as_view() , name='create_product')
]
