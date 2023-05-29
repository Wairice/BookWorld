from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Bookks, Cart, CartItem

admin.site.register(Bookks)
admin.site.register(Cart)
admin.site.register(CartItem)

"""
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Bookks)
class BookksAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"
"""
