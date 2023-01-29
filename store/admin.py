from django.contrib import admin
from .models import CategoryProduct, Product, Images


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'name', 'image',)
    list_display_links = ('id', 'name', 'product',)
    search_fields = ('name', 'product',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'name', 'description', 'characteristics', 'available_status', 'quantity_in_stock', 'price',
        'created_at', 'updated_at',)
    list_display_links = ('id', 'name', 'category',)
    search_fields = ('name',)
    inlines = [ProductImageInline]


# Register your models here.
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
