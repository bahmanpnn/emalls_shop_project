from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
class registerform(forms.Form):
    email=forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
               ]
                           )
    password=forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
                             )
    confirm_password=forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور با تکرار کلمه عبور مغایرت دارد')
class loginform(forms.Form):
    email=forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
               ]
                           )
    password=forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
               ]
                             )
class passwordform(forms.Form):
    email=forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
               ]
    )
class resetpasswordform(forms.Form):
    password=forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
                             )
    confirm_password=forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور با تکرار کلمه عبور مغایرت دارد')