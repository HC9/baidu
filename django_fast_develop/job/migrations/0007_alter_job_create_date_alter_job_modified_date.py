# Generated by Django 4.1.1 on 2022-09-25 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20220923_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 18, 43, 31, 95346), verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 18, 43, 31, 95346), verbose_name='修改时间'),
        ),
    ]