# Generated by Django 3.2.13 on 2022-08-18 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_module', '0007_productbrand_url_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='آی پی کاربری که مشاهده کرده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول بازدید شده')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'بازدید محصول',
                'verbose_name_plural': 'بازدید های محصول',
                'db_table': '',
                'managed': True,
            },
        ),
    ]