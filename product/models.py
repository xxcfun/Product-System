from django.db import models

# Create your models here.
from order.models import Order
from user.models import User


class Product(models.Model):
    # 外键关联订单
    order = models.ForeignKey(Order, verbose_name='生产订单', related_name='products', on_delete=models.CASCADE)
    # 外键关联生产人员
    user = models.ForeignKey(User, verbose_name='生产人员', related_name='products', on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.order

    class Meta:
        db_table = 'product'
        verbose_name = verbose_name_plural = '所有生产信息'
        ordering = ['-created_time']
