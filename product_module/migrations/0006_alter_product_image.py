# Generated by Django 3.2.13 on 2022-05-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='عکس محصول'),
        ),
    ]
