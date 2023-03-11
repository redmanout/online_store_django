from django.contrib import admin

from order.models import StoreCart, OrderProduct, Order


# Register your models here.
@admin.register(StoreCart)
class StoreCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'amount',)
    list_display_links = ('user', 'product', 'quantity',)
    search_fields = ('user', 'product',)
    list_filter = ('user',)


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    can_delete = False
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'city', 'total', 'status', 'create_at', 'update_at',)
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('status', 'first_name', 'phone', 'city',)
    list_filter = ('status',)
    readonly_fields = ('user', 'address', 'city', 'country', 'phone', 'first_name', 'last_name', 'ip', 'total',)
    inlines = [OrderProductInline]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'amount',)
    list_filter = ('user',)
