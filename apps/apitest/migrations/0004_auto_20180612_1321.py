# Generated by Django 2.0.6 on 2018-06-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0003_auto_20180612_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='update_time',
            field=models.DateField(default=None, verbose_name='更新时间'),
        ),
    ]