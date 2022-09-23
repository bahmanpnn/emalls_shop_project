from product_module.models import Product
from django.db import models
from account_module.models import user
# Create your models here.
class order(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,verbose_name='کاربر')
    is_paid=models.BooleanField(verbose_name='نهایی شده/نشده')
    payment_date=models.DateField(null=True,blank=True,verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name = 'سبد خرید کاربر'
        verbose_name_plural = 'سبدهای خرید کاربر'
    def calculate_total_price(self):
        total_cost=0
        if self.is_paid:
            for order_detail in self.order_detail_set.all():
                total_cost+=(order_detail.final_price)*(order_detail.count)
        else:
            for order_detail in self.order_detail_set.all():
                total_cost+=(order_detail.product.price)*(order_detail.count)
        return total_cost
    

class order_detail(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE,verbose_name='سبد خرید')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    final_price=models.IntegerField(null=True,blank=True,verbose_name='قیمت نهایی تکی محصول')
    count=models.IntegerField(verbose_name='تعداد')
    def __str__(self):
        return str(self.order)
    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
    def get_total_price(self):
        return (self.count)*(self.product.price)