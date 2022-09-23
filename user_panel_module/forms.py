from django import forms
from account_module.models import user
from django.core import validators
from django.core.exceptions import ValidationError

class edit_profile_form(forms.ModelForm):
    class Meta:
        model = user
        fields =['first_name','last_name','avatar','mobile','adress','about_user']
        widgets={
            'first_name':forms.TextInput(attrs={
                    'class':'form-control'
                }),
            'last_name':forms.TextInput(attrs={
                    'class':'form-control'
                }),
            'avatar':forms.FileInput(attrs={
                    'class':'form-control'
                }),
            'adress':forms.Textarea(attrs={
                    'class':'form-control',
                    'rows':3,
                }),
            'about_user':forms.Textarea(attrs={
                    'class':'form-control',
                    'rows':6,
                }),

            'mobile':forms.TextInput(attrs={
                    'class':'form-control'
                }),
        }
        labels={
            'first_name':'نام',
            'last_name':' نام خانوادگی',
            'avatar':'تصویر پروفایل',
            'adress':'آدرس',
            'mobile':'شماره تماس',
            'about_user':'درباره کاربر',
        }
class change_password_form(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')