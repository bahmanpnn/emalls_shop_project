from product_module.models import Product
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from .models import order,order_detail
# Create your views here.
def add_product_to_basket(request:HttpRequest):
    product_id=int(request.GET.get('product_id'))
    count=int(request.GET.get('count'))
    if count<1:
        return JsonResponse({
            'status':'invalid_count',
            'text': 'تعداد وارد شده درست نیست!',
            'confirmButtonText':'باشه!',
            'icon':'warning'      
        })
    # print(f'product_id is={product_id} and count is={count}')

    if request.user.is_authenticated:
        product=Product.objects.filter(id=product_id,is_active=True,is_delete=False).first()
        if product is not None:
            current_order,created=order.objects.get_or_create(is_paid=False,user_id=request.user.id)
            current_order_detail=current_order.order_detail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count+=count
                current_order_detail.save()
            
            else:
                new_detail=order_detail(order_id=current_order.id,product_id=product_id,count=count)
                new_detail.save()
            
            return JsonResponse({
                'status':"success",
                'text': 'محصول شما با موفقیت ثبت شد',
                'confirmButtonText':'باشه',
                'icon':'success'  
            })
        else:
            return JsonResponse({
                'status':"product not found",
                'text': 'محصول شما یافت نشد!',
                'confirmButtonText':'باشه',
                'icon':'error'  
            })
    else:
        return JsonResponse({
            'status':'not_authenticated',
            'text': 'برای ثبت محصول در سبد خرید ابتدا باید وارد شوید',
            'confirmButtonText':'برو بریم',
            'icon':'error'  
        })
    