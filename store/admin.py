from django.contrib import admin
from .models import CategoryProduct, Product


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'characteristics', 'available_status', 'quantity_in_stock', 'price',
                    'created_at', 'updated_at', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'characteristics')


# Register your models here.
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Product, ProductAdmin)
