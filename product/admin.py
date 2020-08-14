from django.contrib import admin
from .models import Category, Item, Gallery


class GalleryInline(admin.StackedInline):
    model = Gallery


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'featured_image']
    inlines = [GalleryInline]


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Gallery)