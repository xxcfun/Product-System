from django.db import models

# Create your models here.
from order.models import Order
from user.models import User
from utils import constants


class Product(models.Model):
    order = models.ForeignKey(Order, verbose_name='生产订单', related_name='products', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='生产人员', related_name='products', on_delete=models.CASCADE)
    owen_num = models.IntegerField('生产数量')
    status = models.SmallIntegerField('生产状态', choices=constants.PROD_STATUS, default=constants.PROD_BL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'product'
        verbose_name = verbose_name_plural = '所有生产信息'
        ordering = ['-created_time']
