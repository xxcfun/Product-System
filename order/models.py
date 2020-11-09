from django.db import models

# Create your models here.
from django.db.models import F


class Order(models.Model):
    sn = models.CharField('订单编号', max_length=32, blank=True, null=True, unique=True)
    customer = models.CharField('客户名称', max_length=64)
    good = models.CharField('产品名称', max_length=128)
    remark = models.CharField('料号信息', max_length=256, blank=True, null=True)
    sumnumber = models.IntegerField('数量')
    salesperson = models.CharField('业务姓名', max_length=64)
    created_time = models.CharField('创建时间', max_length=128)
    deliver_time = models.CharField('预计发货时间', max_length=128, blank=True, null=True)
    is_valid = models.BooleanField('订单是否存在', default=True)
    is_deliver = models.BooleanField('订单是否已完成', default=False)

    def __str__(self):
        return "客户名称：" + self.customer + "|" + "货品名称：" + self.good

    class Meta:
        db_table = 'order_list'
        verbose_name = verbose_name_plural = '所有订单信息'
        ordering = ['-created_time']

    def update_number(self, count):
        """更改订单产品的数量信息"""
        self.sumnumber = F('sumnumber') - count
        self.save()
        if self.sumnumber == 0:
            self.is_valid = False
            self.save()
            self.refresh_from_db()
        self.refresh_from_db()
