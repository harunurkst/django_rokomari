from django.contrib import admin
from .models import Category, Item, Gallery, Cart, CartItem


class GalleryInline(admin.StackedInline):
    model = Gallery


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'featured_image']
    inlines = [GalleryInline]


class CartInline(admin.StackedInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartInline]


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Gallery)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)