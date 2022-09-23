import queue
from urllib import request
from django.shortcuts import render,redirect
# Create your views here.
from django.views.generic import TemplateView,ListView
from django.http import HttpRequest,JsonResponse,Http404
from django.views import View
from .forms import edit_profile_form,change_password_form
from account_module.models import user
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from order_module.models import order,order_detail
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator

method_decorator(login_required,name='dispatch')
class user_panel_dashboard_page(TemplateView):
    template_name='user_panel_module/user_panel.html'
method_decorator(login_required,name='dispatch')
class shopping_history(ListView):
    model=order
    template_name='user_panel_module/shopping_history.html'
    def get_queryset(self):
        queryset=super().get_queryset()
        request:HttpRequest=self.request
        queryset=queryset.filter(user_id=request.user.id,is_paid=True)
        return queryset
    
@login_required
def user_panel_menu_component(request:HttpRequest):
    return render(request,'user_panel_module/components/user_panel_menu_component.html')
method_decorator(login_required,name='dispatch')
class edit_user_profile_page(View):
    def get(self,request:HttpRequest):
        current_user=user.objects.filter(id=request.user.id).first()
        edit_form=edit_profile_form(instance=current_user)
        context={
            'form':edit_form,
            'current_user':current_user
        }
        return render(request,'user_panel_module/edit_profile_page.html',context)
        
    def post(self,request:HttpRequest):
        current_user=user.objects.filter(id=request.user.id).first()
        edit_form=edit_profile_form(request.POST,request.FILES,instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context={
            'form':edit_form,
            'current_user':current_user
        }
        return render(request,'user_panel_module/edit_profile_page.html',context)
method_decorator(login_required,name='dispatch')
class change_password(View):
    def get(self, request: HttpRequest):
        context = {
            'form': change_password_form()
        }
        return render(request, 'user_panel_module/change_password.html', context)

    def post(self, request: HttpRequest):
        form = change_password_form(request.POST)
        if form.is_valid():
            current_user: user = user.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه می باشد')

        context = {
            'form': form
        }
        return render(request, 'user_panel_module/change_password.html', context)
@login_required
def user_basket(request:HttpRequest):
    current_order,created=order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,user_id=request.user.id)
    total_cost=current_order.calculate_total_price()
    context={
        'order':current_order,
        'total':total_cost
    }
    return render(request,'user_panel_module/user_basket.html',context)
@login_required
def remove_order_detail(request):
    detail_id=request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status':'not_found_detail_id'
        })
    # current_order,created=order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,user_id=request.user.id)
    # detail=current_order.order_detail_set.filter(id=detail_id).first()
    deleted_count,deleted_dict=order_detail.objects.filter(id=detail_id,order__is_paid=False,order__user_id=request.user.id).delete()
    # khate bala mige ordere in id ro mikhaym objectesh hazf beshe baraye orderi ke pardakht nashode va hamchenin baraye hamin user bashe
    if deleted_count ==0:
        return JsonResponse({
            'status':'detail_not_found'
        })
    # else:
    #     detail.delete()
    current_order,created=order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,user_id=request.user.id)
    total_cost=current_order.calculate_total_price()
    context={
        'order':current_order,
        'total':total_cost
    }
    data=render_to_string('user_panel_module/user_basket_content.html',context) 
    return JsonResponse({
        'status':'success',
        'body':data
    })
@login_required
def change_order_detail(request:HttpRequest):
    detail_id=request.GET.get('detail_id')
    state=request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status':'not_found_detail_id_or_state'
        })
    orderdetail=order_detail.objects.filter(id=detail_id,order__user_id=request.user.id,order__is_paid=False)
    if orderdetail is None:
        return JsonResponse({
            'status':'detail_not_found'
        })
    if state=='increase':
        orderdetail.count+=1
        orderdetail.save()
    elif state=='decrease':
        if orderdetail.count==1:
            orderdetail.delete()
        else:
            orderdetail.count+=(-1)
            orderdetail.save()
    else:
        return JsonResponse({
            'status':'state_invalid'
            })
    current_order,created=order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,user_id=request.user.id).first()
    total_cost=current_order.calculate_total_price()
    context={
        'order':current_order,
        'total':total_cost
    }
    data=render_to_string('user_panel_module/user_basket_content.html',context) 
    return JsonResponse({
        'status':'success',
        'body':data
    })
@login_required
def shopping_detail_history(request:HttpRequest,order_id):
    Order=order.objects.prefetch_related('order_detail_set').filter(id=order_id,user_id=request.user.id).first()
    if Order is None:
        raise Http404('سبد خرید مورد نظر یافت نشد!')
    return render(request,'user_panel_module/shopping_detail_history.html',{
        'Order':Order
    })