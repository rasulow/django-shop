from django.contrib import admin
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'user']

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Order._meta.get_fields()]
    list_filter = ['status']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)

