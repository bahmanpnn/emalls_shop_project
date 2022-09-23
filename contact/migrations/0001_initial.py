# Generated by Django 3.2.6 on 2022-04-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, null=True, verbose_name='عنوان')),
                ('email', models.CharField(max_length=300, verbose_name='ایمیل')),
                ('fullname', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('message', models.TextField(verbose_name='متن تماس با ما')),
                ('is_read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شدن توسط ادمین')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('response', models.TextField(null=True, verbose_name='متن پاسخ ادمین')),
            ],
            options={
                'verbose_name': 'مخاطب',
                'verbose_name_plural': 'مخاطبین',
            },
        ),
    ]
