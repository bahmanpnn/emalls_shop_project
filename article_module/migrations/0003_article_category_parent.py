# Generated by Django 3.2.13 on 2022-05-16 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_alter_article_category_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.article_category'),
        ),
    ]
