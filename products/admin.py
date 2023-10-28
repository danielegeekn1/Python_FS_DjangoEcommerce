from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'provision')

# Register your models here.
admin.site.register(Products, ProductsAdmin)
