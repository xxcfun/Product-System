import datetime

from django.db import models

# Create your models here.
from django.utils import timezone

from user.models import User


class Product(models.Model):
    PROD_STATUS = {
        (1, '备料'),
        (2, '派单'),
        (3, '生产中'),
        (4, '待发货'),
        (5, '订单完成'),
    }
    customer = models.CharField('客户名称', max_length=64)
    good = models.CharField('货品名称', max_length=128)
    deliver_time = models.CharField('发货时间', max_length=128)
    number = models.IntegerField('数量')
    status = models.SmallIntegerField('订单状态', choices=PROD_STATUS)
    is_valid = models.BooleanField('订单是否作废', default=True)
    deliver = models.BooleanField('订单是否完成', default=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)
    # is_overdue = models.BooleanField('是否超期', default=False)
    user = models.ForeignKey(User, verbose_name='负责人', on_delete=models.CASCADE)

    def __str__(self):
        return "客户名称:" + self.customer + "|" + "货品名称:" + self.good

    class Meta:
        db_table = 'product'
        verbose_name = verbose_name_plural = '生产信息'
        ordering = ['-created_time']
