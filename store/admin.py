from django.contrib import admin
from .models import *


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'slug',)
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
        'created_at', 'updated_at', 'slug',)
    list_display_links = ('id', 'name', 'category',)
    search_fields = ('name',)
    inlines = [ProductImageInline]


class BladesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueBladesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'handle_type', 'composition', 'size',)


class RubbersProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueRubbersAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'speed_type',)


class BallsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueBallsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'rank', 'package',)


class BackpacksBagsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueBackpacksBagsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'color',)


class NetsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueNetsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'color',)


class TablesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueTablesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'section', 'color', 'thickness',)


class RacketsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueRacketsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'handle_type', 'average_weight', 'rubbers_thickness',)


class AccessoriesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ValueAccessoriesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'color',)


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
admin.site.register(RubbersProductAttribute, RubbersProductAttributeAdmin)
admin.site.register(ValueRubbersAttribute, ValueRubbersAttributeAdmin)
admin.site.register(RubbersBrand)
admin.site.register(RubbersType)
admin.site.register(RubbersSpeedType)
admin.site.register(BallsProductAttribute, BallsProductAttributeAdmin)
admin.site.register(ValueBallsAttribute, ValueBallsAttributeAdmin)
admin.site.register(BallsBrand)
admin.site.register(BallsRank)
admin.site.register(BallsPackage)
admin.site.register(BackpacksBagsProductAttribute, BackpacksBagsProductAttributeAdmin)
admin.site.register(ValueBackpacksBagsAttribute, ValueBackpacksBagsAttributeAdmin)
admin.site.register(BackpacksBagsBrand)
admin.site.register(BackpacksBagsType)
admin.site.register(BackpacksBagsColor)
admin.site.register(NetsProductAttribute, NetsProductAttributeAdmin)
admin.site.register(ValueNetsAttribute, ValueNetsAttributeAdmin)
admin.site.register(NetsBrand)
admin.site.register(NetsColor)
admin.site.register(TablesProductAttribute, TablesProductAttributeAdmin)
admin.site.register(ValueTablesAttribute, ValueTablesAttributeAdmin)
admin.site.register(TablesBrand)
admin.site.register(TablesSection)
admin.site.register(TablesColor)
admin.site.register(TablesThickness)
admin.site.register(RacketsProductAttribute, RacketsProductAttributeAdmin)
admin.site.register(ValueRacketsAttribute, ValueRacketsAttributeAdmin)
admin.site.register(RacketsBrand)
admin.site.register(RacketsType)
admin.site.register(RacketsHandleType)
admin.site.register(RacketsAverageWeight)
admin.site.register(RacketsRubbersThickness)
admin.site.register(AccessoriesProductAttribute, AccessoriesProductAttributeAdmin)
admin.site.register(ValueAccessoriesAttribute, ValueAccessoriesAttributeAdmin)
admin.site.register(AccessoriesBrand)
admin.site.register(AccessoriesType)
admin.site.register(AccessoriesColor)
