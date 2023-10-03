from django.contrib import admin

from catalog.models import Categories, Products, Contacts, Version


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)  # id, название, цена и категория
    list_filter = ('category',)  # фильтровать по категории
    search_fields = ('product_name', 'description',)  # поиск по названию и полю описания.

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Contacts)

admin.site.register(Version)


