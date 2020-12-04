# Generated by Django 2.2.16 on 2020-12-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20201203_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.SmallIntegerField(choices=[(1, '备料中'), (3, '生产中'), (2, '待生产'), (4, '待发货')], default=2, verbose_name='订单状态'),
        ),
    ]