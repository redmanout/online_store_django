from django.contrib import admin
from .models import *


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'image',)
    list_display_links = ('id', 'product',)
    search_fields = ('name', 'product',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'name', 'description', 'characteristics', 'available_status', 'quantity_in_stock', 'price',
        'created_at', 'updated_at',)
    list_display_links = ('id', 'name', 'category',)
    search_fields = ('name',)
    inlines = [ProductImageInline]


class BladesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueBladesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'handle_type', 'composition', 'size',)


# Register your models here.
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(BladesProductAttribute, BladesProductAttributeAdmin)
admin.site.register(ValueBladesAttribute, ValueBladesAttributeAdmin)
admin.site.register(BladesBrand)
admin.site.register(BladesType)
admin.site.register(BladesHandleType)
admin.site.register(BladesComposition)
admin.site.register(BladesSize)
