# Generated by Django 4.1 on 2022-08-29 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 29, 13, 15, 13, 187450), verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 29, 13, 15, 13, 187450), verbose_name='修改时间'),
        ),
    ]
