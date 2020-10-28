# Generated by Django 2.2.16 on 2020-10-28 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_delete_record'),
        ('user', '0001_initial'),
        ('product', '0003_auto_20201027_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=64, verbose_name='客户名称')),
                ('good', models.CharField(max_length=128, verbose_name='产品名称')),
                ('deliver_time', models.CharField(max_length=128, verbose_name='预计发货时间')),
                ('number', models.IntegerField(verbose_name='数量')),
                ('salesperson', models.CharField(max_length=64, verbose_name='业务姓名')),
                ('is_valid', models.BooleanField(default=True, verbose_name='订单是否存在')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '生产订单信息',
                'verbose_name_plural': '生产订单信息',
                'db_table': 'order_list',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owen_num', models.IntegerField(verbose_name='生产数量')),
                ('status', models.SmallIntegerField(choices=[(3, '待发货'), (4, '订单完成'), (2, '生产中'), (1, '备料')], default=1, verbose_name='生产状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.OrderList', verbose_name='生产订单')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='生产人员')),
            ],
            options={
                'db_table': 'product_list',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
