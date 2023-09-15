from django.urls import path

from catalog import views
from catalog.views import index, ProductsDetailView, CatalogListView, ContactsView



urlpatterns = [
    path('', index),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductsDetailView.as_view(), name='product'),
]
