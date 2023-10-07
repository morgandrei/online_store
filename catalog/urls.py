from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog import views
from catalog.views import index, ProductsDetailView, CatalogListView, ContactsView, BlogCreateView, BlogListView, \
    BlogUpdateView, BlogDetailView, BlogDeleteView, toggle_activity, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('blog/', BlogListView.as_view(), name='list'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('product/create/', never_cache(ProductsCreateView.as_view()), name='product_create'),
    path('product/<int:pk>', cache_page(60)(ProductsDetailView.as_view()), name='product'),
    path('product/<int:pk>/update/', ProductsUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),

]
