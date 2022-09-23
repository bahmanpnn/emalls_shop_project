
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account_module.models import user

# Create your models here.
class ProductBrand(models.Model):
    title=models.CharField(max_length=300,verbose_name='نام برند',db_index=True)
    url_title=models.CharField(max_length=300,verbose_name='نام در  url',db_index=True)
    is_active=models.BooleanField(null=True,verbose_name='فعال/غیر فعال')
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'
    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Product(models.Model):
    image=models.ImageField(upload_to='images/products',null=True,blank=True,verbose_name='عکس محصول')
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    brand=models.ForeignKey(ProductBrand,on_delete=models.CASCADE,related_name='product_brand',null=True)
    category = models.ManyToManyField(ProductCategory,related_name='product_categories',verbose_name='دسته بندی ها')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption

class product_visit(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE,verbose_name='محصول بازدید شده')
    ip=models.CharField(max_length=30,verbose_name='آی پی کاربری که مشاهده کرده')
    user=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE,verbose_name='کاربر')
    def __str__(self):
        return f'{self.product.title}/{self.ip}'
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'

class product_gallery_images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    # in ghesmate imagefield ro yad begir height_field=75, width_field=75
    image=models.ImageField(upload_to='images/product_gallery',verbose_name='عکص محصول')
    def __str__(self):
        return self.product.title
    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری'

class product_comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    parent=models.ForeignKey('product_comment',null=True,blank=True,on_delete=models.CASCADE,verbose_name='والد دارد یا نه')
    user=models.ForeignKey(user,on_delete=models.CASCADE,verbose_name='کاربر')
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت کامنت')
    text=models.TextField(verbose_name='متن  کامنت')
    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'