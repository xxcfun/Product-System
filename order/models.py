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
    sumnumber = models.IntegerField('数量')   # 无意义
    salesperson = models.CharField('业务姓名', max_length=64)
    created_time = models.CharField('创建时间', max_length=128)
    order_date = models.CharField('时间', max_length=16, blank=True, null=True)
    deliver_time = models.CharField('预计发货时间', max_length=128, blank=True, null=True)
    # 下面为系统自定义的字段
    # 当生产结束时，订单转为不存在，不在界面上显示
    is_valid = models.BooleanField('订单是否存在', default=True)
    """
    读取sqlserver中的数据存入数据库时，状态默认为待生产
    生产开始生产时，状态改为生产中
    待该订单全部生产完成时，改为待出货
    所有出货完成后，将is_valid字段改为false
    """
    order_status = models.SmallIntegerField('订单状态', choices=constants.ORDER_STATUS, default=constants.ORDER_DSC)

    def __str__(self):
        return "客户名称：" + self.customer + "|" + "货品名称：" + self.good

    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '所有订单信息'
        ordering = ['-order_id']

    def update_number(self, count):
        """更改订单产品的数量信息"""
        self.sumnumber = F('sumnumber') - count
        self.save()
        if self.sumnumber == 0:
            self.is_valid = False
            self.save()
            self.refresh_from_db()
        self.refresh_from_db()

    def update_status_scz(self):
        """当订单开始生产时，状态改为生产中"""
        self.order_status = constants.ORDER_SCZ
        self.save()
        self.refresh_from_db()

    def update_status_dfh(self):
        """当生产结束了，状态改为待发货"""
        self.order_status = constants.ORDER_DFH
        self.save()
        self.refresh_from_db()

    def update_status_ddwc(self):
        """当发货完成时，订单完成，将is_valid字段改为false"""
        self.is_valid = False
        self.save()
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
