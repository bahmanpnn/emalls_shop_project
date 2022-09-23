from django import template
from jalali_date import date2jalali
register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    ''' removes all values of arg from the given string'''
    return  value.replace(arg,'')
# register.filter('cut',cut)
@register.filter(name='show_jalali_date')
def show_jalali_date(value):
    return date2jalali(value)
@register.filter(name='three_digits_currency')
def three_digits_currency(value:int):
    return '{:,}'.format(value)+' تومان '
@register.filter(name='etc')
def etc(text,char=22):
    txt=''
    for i in range(char):
        txt+=text[i]
    last_txt=txt+'...'
    return(last_txt)
@register.filter(name='multiply')
def multiply(quantity,price,*args, **kwargs):
    return three_digits_currency(quantity*price)