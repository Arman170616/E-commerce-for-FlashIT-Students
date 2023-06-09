from django.contrib import admin

from .models import Category, Product, ProductImages



class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)


