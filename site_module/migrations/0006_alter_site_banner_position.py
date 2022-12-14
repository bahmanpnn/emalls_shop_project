# Generated by Django 3.2.13 on 2022-08-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_site_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_banner',
            name='position',
            field=models.CharField(choices=[('product_list', 'صفحه محصولات'), ('product_detail', 'صفحه جزییات محصولات'), ('about_us', 'درباره ما'), ('contact_us', 'تماس با ما'), ('article_page', 'صفحه مقالات'), ('articles_detail_page', 'صفحه جزییات مقاله')], max_length=200, verbose_name='جایگاه نمایشی'),
        ),
    ]
