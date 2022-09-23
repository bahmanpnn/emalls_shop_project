from django import forms
from .models import contact


class contact_us_model_form(forms.ModelForm):
    
    class Meta:
        model = contact
        fields =['title','fullname','email','message']
        widgets={
            'fullname':forms.TextInput(attrs={
                    'class':'form-control'
                }),
            'email':forms.EmailInput(attrs={
                    'class':'form-control'
                }),
            'title':forms.TextInput(attrs={
                    'class':'form-control'
                }),
            'message':forms.Textarea(attrs={
                    'class':'form-control',
                    'rows':5,
                    'id':'message'
                }),
        }
        labels={
            'fullname':'نام و نام خانوادگی',
            'email':'ایمیل',
            'title':'موضوع شما',
            'message':'متن پیام شما'
        }
        error_messages={
            'fullname':{
                'required':'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length':'تعداد کارکتر نباید بیشتر از 60 تا باشد!'
            },
            'email':{
                'required':'لطفا ایمیل خود را وارد کنید'
            },
            'title':{
                'required':'لطفا موضوع خود را وارد کنید',
                'max_length':'تعداد کارکتر نباید بیشتر از 60 تا باشد!'
            },
            'message':{
                'required':'لطفا پیام خود را وارد کنید'
            }
        }
