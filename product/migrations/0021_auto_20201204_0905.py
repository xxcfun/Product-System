# Generated by Django 2.2.16 on 2020-12-04 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20201203_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(3, '待发货'), (2, '生产中'), (4, '订单完成'), (1, '备料中')], default=1, verbose_name='生产状态'),
        ),
    ]
