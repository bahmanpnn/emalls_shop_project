# Generated by Django 3.2.13 on 2022-08-14 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0007_article_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article_comment',
            options={'verbose_name': 'نظر و کامنت', 'verbose_name_plural': 'نظرات و کامنت ها'},
        ),
    ]
