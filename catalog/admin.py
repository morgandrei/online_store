from django.contrib import admin

from catalog.models import Categories, Products


@admin.register(Categories)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class StudentAdmin(admin.ModelAdmin):
    pass