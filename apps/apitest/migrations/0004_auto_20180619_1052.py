# Generated by Django 2.0.6 on 2018-06-19 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0003_auto_20180619_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='add_time',
            field=models.DateField(blank=True, null=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='update_time',
            field=models.DateField(blank=True, null=True, verbose_name='更新时间'),
        ),
    ]