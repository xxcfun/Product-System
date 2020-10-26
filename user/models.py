from django.db import models

# Create your models here.


# class Power(models.Model):
#     dist = models.CharField('操作', max_length=64)


class User(models.Model):
    name = models.CharField('用户名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    beiliao = models.BooleanField('备料', default=False)
    paidan = models.BooleanField('派单', default=False)
    shengchanzhong = models.BooleanField('生产中', default=False)
    wancheng = models.BooleanField('订单完成', default=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # power = models.ManyToManyField(Power, verbose_name='权限')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = '用户'
        db_table = 'user'
