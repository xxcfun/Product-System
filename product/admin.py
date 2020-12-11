from django.contrib import admin

# Register your models here.
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'created_time', 'updated_time')
    list_per_page = 10
    ordering = ['-created_time']
