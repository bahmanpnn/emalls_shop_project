from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse,HttpRequest
from django.shortcuts import redirect
import requests
import json
import time
from django.contrib.auth.decorators import login_required
from order_module.models import order,order_detail
MERCHANT = ''
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "نهایی کردن خرید شما از سایت ما"  # Required
email = ''  # Optional
mobile = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zarin_pal/verify/'
@login_required
def send_request(request:HttpRequest):
    current_order,created=order.objects.get_or_create(is_paid=False,user_id=request.user.id)
    total_price=current_order.calculate_total_price() 
    if total_price==0:
        return redirect(reverse('user_basket_page'))
    
    req_data = {
        "merchant_id": MERCHANT,
        "amount":total_price*10,
        "callback_url": CallbackURL,
        "description": description,
        # "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"
                  }
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

@login_required
def verify(request:HttpRequest):
    current_order,created=order.objects.get_or_create(is_paid=False,user_id=request.user.id)
    total_price=current_order.calculate_total_price() 
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if t_status == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": total_price*10,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                # return HttpResponse('Transaction success.\nRefID: ' + str(
                #     req.json()['data']['ref_id']
                # ))
                current_order.is_paid=True
                current_order.payment_date=time.time
                current_order.save()
                ref_str=req.json()['data']['ref_id']
                return render(request,'zarin_pal_module/payment_result.html',{
                    'success':f'تراکنش شما با کد پیگیری{ref_str}با موفقیت انجام شد'
                })
            elif t_status == 101:
                # return HttpResponse('Transaction submitted : ' + str(
                #     req.json()['data']['message']
                # ))
                return render(request,'zarin_pal_module/payment_result.html',{
                    'info':'این تراکنش قبلا ثبت شده است'
                })
            else:
                # return HttpResponse('Transaction failed.\nStatus: ' + str(
                #     req.json()['data']['message']
                # ))
                    return render(request,'zarin_pal_module/payment_result.html',{
                    'error':str(req.json()['data']['message'])
                })
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            # return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
            return render(request,'zarin_pal_module/payment_result.html',{
                'error':e_message
                })
    else:
        # return HttpResponse('Transaction failed or canceled by user')
        return render(request,'zarin_pal_module/payment_result.html',{
                    'error':'پرداخت با خطا مواجه شد یا کاربر از پرداخت ممانعت کرد'
                })