# Generated by Django 2.2.16 on 2020-10-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deliver',
            field=models.BooleanField(default=False, verbose_name='订单是否完成'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='订单是否作废'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(5, '订单完成'), (1, '备料'), (3, '生产中'), (4, '待发货'), (2, '派单')], verbose_name='订单状态'),
        ),
    ]
