# Generated by Django 4.1 on 2022-08-29 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_create_date_alter_job_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 29, 13, 17, 22, 1984), verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 29, 13, 17, 22, 1984), verbose_name='修改时间'),
        ),
    ]
