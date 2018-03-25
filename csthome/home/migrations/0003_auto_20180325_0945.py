# Generated by Django 2.0.2 on 2018-03-25 09:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_event_some_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-created',), 'verbose_name': '活动', 'verbose_name_plural': '活动'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created',), 'verbose_name': '新闻', 'verbose_name_plural': '新闻'},
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True, verbose_name='链接'),
        ),
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='event',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='正文'),
        ),
    ]
