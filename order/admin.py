from django.contrib import admin

# Register your models here.
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'good', 'deliver_time', 'number',
                    'salesperson', 'is_valid', 'created_time')
    list_per_page = 10
    ordering = ['-created_time']
    # 添加自定义方法
    actions = ['enable_prod', 'disable_prod']

    def enable_prod(self, request, queryset):
        """批量激活订单"""
        queryset.update(is_valid=True)
    enable_prod.short_description = '批量恢复订单'

    def disable_prod(self, request, queryset):
        """批量禁用订单"""
        queryset.update(is_valid=False)
    disable_prod.short_description = '批量销毁订单'