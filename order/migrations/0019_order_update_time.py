# Generated by Django 2.2.16 on 2020-12-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20201214_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
