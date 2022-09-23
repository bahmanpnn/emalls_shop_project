from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    avatar=models.ImageField(upload_to='images/profiles',null=True,blank=True,verbose_name='عکس کاربر')
    mobile=models.CharField(max_length=20,verbose_name='شماره همراه',null=True,blank=True)
    email_active_code=models.CharField(max_length=100,verbose_name='کد فعالسازی ایمیل')
    about_user=models.TextField(null=True,blank=True,verbose_name='درباره کاربر')
    adress=models.TextField(null=True,blank=True,verbose_name='آدرس')
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':

            return self.get_full_name()
        return self.email
