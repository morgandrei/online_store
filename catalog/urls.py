from django.urls import path

from catalog.views import index, contacts, catalog

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('catalog/', catalog)
]