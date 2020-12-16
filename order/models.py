from django.db import models

# Create your models here.
from django.db.models import F

from utils import constants


class Order(models.Model):
    # 从sqlserver中抓取的信息 所有订单列表
    order_id = models.IntegerField('订单编号', unique=True, primary_key=True)
    customer = models.CharField('客户名称', max_length=64)
    good = models.CharField('产品名称', max_length=128)
    remark = models.CharField('料号信息', max_length=256, blank=True, null=True)
    sumnumber = models.IntegerField('数量')   # 无意义 捕获虚拟库存
    salesperson = models.CharField('业务姓名', max_length=64)
    created_time = models.CharField('创建时间', max_length=128)
    order_date = models.CharField('时间', max_length=16, blank=True, null=True)
    deliver_time = models.CharField('预计发货时间', max_length=128, blank=True, null=True)

    # 删除时，将该字段的值改为false
    is_valid = models.BooleanField('订单是否存在', default=True)
    # 所有出货完成后，status值转变为4，既订单完成
    order_status = models.SmallIntegerField('订单状态', choices=constants.ORDER_STATUS, default=1)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True, blank=True)

    def __str__(self):
        return "客户名称：" + self.customer + "|" + "货品名称：" + self.good

    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '所有订单信息'
        ordering = ['-order_id']

    """目前这部分不启用"""
    def update_number(self, count):
        """更改订单产品的数量信息"""
        self.sumnumber = F('sumnumber') - count
        self.save()
        if self.sumnumber == 0:
            self.is_valid = False
            self.save()
            self.refresh_from_db()
        self.refresh_from_db()


class OrderList(models.Model):
    """所有订单的配件信息"""
    list_id = models.IntegerField('订单配件id', unique=True, primary_key=True)
    order = models.ForeignKey(Order, related_name='order', verbose_name='订单', on_delete=models.CASCADE)
    good = models.CharField('产品名称', max_length=128)
    good_number = models.IntegerField('数量')

    class Meta:
        db_table = 'order_list'
        verbose_name_plural = verbose_name = '订单配件表'
        ordering = ['list_id']


class OrderBill(models.Model):
    order = models.ForeignKey(Order, related_name='orderbill', verbose_name='订单', on_delete=models.CASCADE)
    odd_number = models.CharField('物流单号', max_length=128, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'order_bill'
        verbose_name_plural = verbose_name = '物流单号表'
        ordering = ['-create_time']
