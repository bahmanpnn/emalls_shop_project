from django.db import models
from account_module.models import user
from jalali_date import datetime2jalali, date2jalali
# Create your models here.
class article_category(models.Model):
    parent=models.ForeignKey('article_category',null=True,blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,verbose_name='عنوان دسته بندی')
    url_title=models.CharField(max_length=200,unique=True,verbose_name='عنوان لینک')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیر فعال بودن دسته بندی مقاله')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='دسته بندی مقاله'
        verbose_name_plural='دسته بندی های مقاله'
class article(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان مقاله')
    slug=models.SlugField(max_length=400,db_index=True,allow_unicode=True,verbose_name='عنوان در url')
    image=models.ImageField(upload_to='images/articles',verbose_name='تصویر اصلی مقاله')
    short_description=models.TextField(verbose_name='توضیحات کوتاه')
    text=models.TextField(verbose_name='متن اصلی مقاله')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیر فعال بودن')
    selected_category=models.ManyToManyField(article_category,verbose_name='دسته بندی ها')
    author=models.ForeignKey(user,on_delete=models.CASCADE,verbose_name='نویسنده',null=True,editable=False)
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='ثبت تاریخ',editable=False)
    def __str__(self):
        return self.title
    def get_jalali_create_date(self):
        return date2jalali(self.create_date)
    def get_jalali_create_datetime(self):
        return self.create_date.strftime('%H:%M')
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'
class article_comment(models.Model):
    article=models.ForeignKey(article,on_delete=models.CASCADE,verbose_name='برای کدام مقاله')
    parent=models.ForeignKey('article_comment',null=True,blank=True,on_delete=models.CASCADE,verbose_name='والد دارد کامنت یا خیر')
    user=models.ForeignKey(user,on_delete=models.CASCADE,verbose_name='کاربر درج کامنت')
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='زمان درج کامنت')
    text=models.TextField(verbose_name='متن کامنت')
    class Meta:
        verbose_name='نظر و کامنت'
        verbose_name_plural='نظرات و کامنت ها'
    def __str__(self):
        return str(self.user)