# Generated by Django 2.0.2 on 2018-03-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180321_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('F', '女'), ('M', '男'), ('U', '未选择')], default='U', max_length=1, verbose_name='性别'),
        ),
    ]
