# Generated by Django 3.2.13 on 2022-05-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0003_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیر فعال'),
        ),
    ]
