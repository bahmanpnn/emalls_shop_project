from django.shortcuts import render
from django.contrib.auth import get_user_model,login,logout
from django.views import View
from account_module.forms import registerform,loginform,passwordform,resetpasswordform
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404,HttpRequest
# Create your views here.
from .models import user
from django.utils.crypto import get_random_string
from utils.email_service import send_email

class register_view(View):
    def get(self,request):
        register_form=registerform()
        context={
            'register_form':register_form
        }
        return render(request,'account_module/register_form.html',context)
    def post(self,request):
        register_form=registerform(request.POST)
        if register_form.is_valid():
            user_password=register_form.cleaned_data.get('password')
            user_email=register_form.cleaned_data.get('email')
            User: bool = user.objects.filter(email__iexact=user_email).exists()
            if User:
                register_form.add_error('email','ایمیل وارد شده تکراری میباشد!')
            else:
                new_user=user(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                #to do send email active code
                send_email('فعالسازی حساب کاربری',new_user.email,{'User':new_user},'emails/active_account.html')
                return redirect(reverse('login_page'))
        context={
            'register_form':register_form
        }
        return render(request,'account_module/register_form.html',context)
class login_view(View):
    def get(self,request):
        login_form=loginform()
        context={
            'login_form':login_form
        }
        return render(request,'account_module/login_form.html',context)
    def post(self,request: HttpRequest):
        login_form=loginform(request.POST)
        if login_form.is_valid():
            user_email=login_form.cleaned_data.get('email')
            user_password=login_form.cleaned_data.get('password')
            User:user=user.objects.filter(email__iexact=user_email).first()
            if User is not None:
                if not User.is_active:
                    login_form.add_error('email','حساب کاربری شما فعال نشده است!')
                else:
                    is_password_correct = User.check_password(user_password)
                    if is_password_correct:
                        login(request,User)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email','ایمیل یا کلمه عبور وارد شده اشتباه است!')
            else:
                login_form.add_error('email','کاربری با مشخصات وارد شده یافت نشد!')
        context={
            'login_form':login_form
        }
        return render(request,'account_module/login_form.html',context)
class activate_account(View):
    def get(self,request,email_active_code):
        User:user=user.objects.filter(email_active_code__iexact=email_active_code).first()
        if User is not None:
            if not user.is_active:
                user.is_active=True
                user.email_active_code=get_random_string(72)
                user.save()
                #to do:show success message to user
                return redirect(reverse('login_page'))
            else:
                #to do:show your account was activated to user
                pass
        else:
            raise Http404
class forget_password_view(View):
    def get(self,request):
        forget_password=passwordform()
        context={
            'forget_password':forget_password
        }
        return render(request,'account_module/forget_password.html',context)
    def post(self,request: HttpRequest):
        forget_password=passwordform(request.POST)
        if forget_password.is_valid():
            user_email=forget_password.cleaned_data.get('email')
            User:user=user.objects.filter(email__iexact=user_email).first()
            if User is not None:
                #be user neshoon midi ke email ba moafaghiat ersal shode
                send_email('بازیابی کلمه عبور',User.email,{'User':User},'emails/forget_password.html')
                return redirect(reverse('login_page'))
            else:
                forget_password.add_error('email','حسابی با این ایمیل وجود ندارد!')

        context={
            'forget_password':forget_password
        }
        return render(request,'account_module/forget_password.html',context)
class reset_password_view(View):
    def get(self,request,active_code):
        User:user=user.objects.filter(email_active_code__iexact=active_code).first()
        if User is None:
            return redirect(reverse('login_page'))

        else:
            reset_password=resetpasswordform()
        context={
            'reset_password':reset_password,
            'User':User
        }
        return render(request,'account_module/reset_password.html',context)
    def post(self,request:HttpRequest,active_code):
        reset_password=resetpasswordform(request.POST)
        User: user = user.objects.filter(email_active_code__iexact=active_code).first()
        if reset_password.is_valid():
            if User is None:
                reset_password.add_error('password','error!')
                return redirect(reverse('login_page'))
            else:
                user_new_password=reset_password.cleaned_data.get('password')
                User.set_password(user_new_password)
                User.email_active_code=get_random_string(72)
                User.is_active=True
                User.save()
                return redirect(reverse('login_page'))
        context={
            'reset_password':reset_password,
            'User':User
        }
        return render(request,'account_module/reset_password.html',context)
class logout_view(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('login_page'))
