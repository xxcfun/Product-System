from django.db import models

# Create your models here.
from product.models import Product
from user.models import User


class Record(models.Model):
    """用户操作日志"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, verbose_name='生产信息', on_delete=models.CASCADE)
    time = models.DateTimeField('操作时间', auto_now_add=True)

    def __str__(self):
        return self.prod

    class Meta:
        db_table = 'record'
        ordering = ['-time']
        verbose_name = verbose_name_plural = '操作日志'
