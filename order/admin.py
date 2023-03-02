from django.contrib import admin

from order.models import StoreCart


# Register your models here.
@admin.register(StoreCart)
class StoreCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'amount',)
    list_display_links = ('user', 'product', 'quantity',)
    search_fields = ('user', 'product',)
    list_filter = ('user',)
