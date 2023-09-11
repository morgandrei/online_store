from django.urls import path

from catalog import views
from catalog.views import index, contacts, catalog, product

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('catalog/', catalog),
    path('product/<int:pk>', product, name='product'),
]
