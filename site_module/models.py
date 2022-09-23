from operator import mod
from django.db import models

# Create your models here.
class site_setting(models.Model):
    site_name=models.CharField(max_length=200,verbose_name='اسم سایت')
    site_url=models.CharField(max_length=200,verbose_name='دامنه سایت')
    address=models.CharField(max_length=200,verbose_name='آدرس')
    phone=models.CharField(max_length=200,verbose_name='شماره تماس',null=True,blank=True)
    fax=models.CharField(max_length=200,verbose_name='شماره فکس',null=True,blank=True)
    email=models.CharField(max_length=200,verbose_name='ایمیل',null=True,blank=True)
    copy_right=models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text=models.TextField(verbose_name='متن درباره ما سایت')
    site_logo=models.ImageField(upload_to='images/site_setting/',verbose_name='لوگو سایت')
    is_main_setting=models.BooleanField(verbose_name='تنظیمات اصلی')
    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='تنظیمات'
    def __str__(self):
        return self.site_name

class footer_link_box(models.Model):
    title=models.CharField(max_length=200,verbose_name='عنوان')
    class Meta:
        verbose_name='دسته بندی لینک های فوتر'
        verbose_name_plural='دسته بندی های لینک های فوتر'
    def __str__(self):
        return self.title
class footer_link(models.Model):

    title=models.CharField(max_length=200,verbose_name='عنوان')
    url=models.URLField(max_length=500,verbose_name='لینک')
    footer_link_box=models.ForeignKey(to=footer_link_box,on_delete=models.CASCADE,verbose_name='دسته بندی')
    class Meta:
        verbose_name='لینک فوتر'
        verbose_name_plural='لینک های فوتر'
    def __str__(self):
        return self.title
class slider(models.Model):
    title=models.CharField(max_length=200,verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description=models.TextField(verbose_name='توضیحات اسلایدر')
    image=models.ImageField(upload_to='images/slider',verbose_name='تصویر اسلایدر')
    is_active=models.BooleanField(verbose_name='فعال/غیر فعال',default=False)
    class Meta:
        verbose_name='اسلایدر'
        verbose_name_plural='اسلایدر ها'
    def __str__(self):
        return self.title
class site_banner(models.Model):
    class site_banner_choices(models.TextChoices):
        product_list='product_list','صفحه محصولات',
        product_detail='product_detail','صفحه جزییات محصولات',
        about_us='about_us','درباره ما',
        contact_us='contact_us','تماس با ما',
        article_page='article_page','صفحه مقالات',
        articles_detail_page='articles_detail_page','صفحه جزییات مقاله'
    title=models.CharField(max_length=200,verbose_name='عنوان بنر')
    url=models.URLField(max_length=400,verbose_name='آدرس بنر',null=True,blank=True)
    image=models.ImageField(upload_to='images/banners',verbose_name='تصویر بنر')
    is_active=models.BooleanField(verbose_name='فعال بودن بنر')
    position=models.CharField(max_length=200,choices=site_banner_choices.choices,verbose_name='جایگاه نمایشی')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'
    