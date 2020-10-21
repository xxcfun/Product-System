from django.db import models

# Create your models here.
from user.models import User


class Product(models.Model):
    PROD_STATUS = {
        ('PROD_MATE', '备料'),
        ('PROD_DIST', '派单'),
        ('PROD_PROD', '生产中'),
        ('PROD_DELE', '待发货'),
        ('PROD_FINS', '订单完成'),
    }
    customer = models.CharField('客户名称', max_length=64)
    good = models.CharField('货品名称', max_length=128)
    deliver_time = models.CharField('发货时间', max_length=128)
    number = models.IntegerField('数量')
    status = models.SmallIntegerField('订单状态', choices=PROD_STATUS)
    is_valid = models.BooleanField('订单是否作废', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(User, verbose_name='负责人', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer + self.good

    class Meta:
        db_table = 'product'
        verbose_name = verbose_name_plural = '生产信息'
        ordering = ['-created_time']
