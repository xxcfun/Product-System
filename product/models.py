from django.db import models

# Create your models here.
from user.models import User
from utils import constants


class OrderList(models.Model):
    customer = models.CharField('客户名称', max_length=64)
    good = models.CharField('产品名称', max_length=128)
    deliver_time = models.CharField('预计发货时间', max_length=128)
    number = models.IntegerField('数量')
    salesperson = models.CharField('业务姓名', max_length=64)
    is_valid = models.BooleanField('订单是否存在', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return "客户名称：" + self.customer + "|" + "货品名称：" + self.good

    class Meta:
        db_table = 'order_list'
        verbose_name = verbose_name_plural = '生产订单信息'
        ordering = ['-created_time']


class ProductList(models.Model):
    order = models.ForeignKey(OrderList, verbose_name='生产订单', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='生产人员', on_delete=models.CASCADE)
    owen_num = models.IntegerField('生产数量')
    status = models.SmallIntegerField('生产状态', choices=constants.PROD_STATUS,
                                      default=constants.PROD_BL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'product_list'
