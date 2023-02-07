from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'slug',)
    list_display_links = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Image'


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'get_image',)
    list_display_links = ('id', 'product',)
    search_fields = ('name', 'product',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Image'


class ReviewProductInline(admin.TabularInline):
    model = ReviewsProduct
    extra = 1
    readonly_fields = ('name', 'email',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'name', 'bestseller', 'new', 'stock', 'available_status',
        'quantity_in_stock', 'price', 'get_image',)
    list_display_links = ('id', 'name', 'category',)
    search_fields = ('name', 'category__name',)
    list_filter = ('category',)
    inlines = [ProductImageInline, ReviewProductInline]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_image',)
    list_editable = ('bestseller', 'new', 'stock', 'available_status', 'quantity_in_stock', 'price',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Image'


@admin.register(ReviewsProduct)
class ReviewsProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'email', 'name', 'text', 'parent',)
    list_display_links = ('id', 'product', 'email',)
    readonly_fields = ('name', 'email',)


@admin.register(BladesProductAttribute)
class BladesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueBladesAttribute)
class ValueBladesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'handle_type', 'composition', 'size',)


@admin.register(RubbersProductAttribute)
class RubbersProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueRubbersAttribute)
class ValueRubbersAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'speed_type',)


@admin.register(BallsProductAttribute)
class BallsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueBallsAttribute)
class ValueBallsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'rank', 'package',)


@admin.register(BackpacksBagsProductAttribute)
class BackpacksBagsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueBackpacksBagsAttribute)
class ValueBackpacksBagsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'color',)


@admin.register(NetsProductAttribute)
class NetsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueNetsAttribute)
class ValueNetsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'color',)


@admin.register(TablesProductAttribute)
class TablesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueTablesAttribute)
class ValueTablesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'section', 'color', 'thickness',)


@admin.register(RacketsProductAttribute)
class RacketsProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueRacketsAttribute)
class ValueRacketsAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'handle_type', 'average_weight', 'rubbers_thickness',)


@admin.register(AccessoriesProductAttribute)
class AccessoriesProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ValueAccessoriesAttribute)
class ValueAccessoriesAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'brand', 'type', 'color',)


@admin.register(RatingStarProduct)
class RatingStarProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'value',)
    list_display_links = ('id', 'value',)


@admin.register(RatingProduct)
class RatingProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'product', 'star',)
    list_display_links = ('id', 'product', 'star',)


admin.site.site_title = 'Django Store'
admin.site.site_header = 'Django Store'

# Register your models here.
admin.site.register(BladesBrand)
admin.site.register(BladesType)
admin.site.register(BladesHandleType)
admin.site.register(BladesComposition)
admin.site.register(BladesSize)
admin.site.register(RubbersBrand)
admin.site.register(RubbersType)
admin.site.register(RubbersSpeedType)
admin.site.register(BallsBrand)
admin.site.register(BallsRank)
admin.site.register(BallsPackage)
admin.site.register(BackpacksBagsBrand)
admin.site.register(BackpacksBagsType)
admin.site.register(BackpacksBagsColor)
admin.site.register(NetsBrand)
admin.site.register(NetsColor)
admin.site.register(TablesBrand)
admin.site.register(TablesSection)
admin.site.register(TablesColor)
admin.site.register(TablesThickness)
admin.site.register(RacketsBrand)
admin.site.register(RacketsType)
admin.site.register(RacketsHandleType)
admin.site.register(RacketsAverageWeight)
admin.site.register(RacketsRubbersThickness)
admin.site.register(AccessoriesBrand)
admin.site.register(AccessoriesType)
admin.site.register(AccessoriesColor)
