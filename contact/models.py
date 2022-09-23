from django.db import models

# Create your models here.
class contact(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان',null=True,db_index=True)
    email=models.CharField(max_length=300,verbose_name='ایمیل')
    fullname=models.CharField(max_length=300,verbose_name='نام و نام خانوادگی')
    message=models.TextField(verbose_name='متن تماس با ما')
    created_date=models.DateTimeField(verbose_name='تاریخ ایجاد',auto_now_add=True)
    response=models.TextField(verbose_name='متن پاسخ ادمین',null=True)
    is_read_by_admin=models.BooleanField(verbose_name='خوانده شدن توسط ادمین',default=False)
    class Meta:
        verbose_name = 'مخاطب'
        verbose_name_plural = 'مخاطبین'
    def __str__(self):
        return self.title
class user_profile(models.Model):
    image=models.ImageField(upload_to='images')