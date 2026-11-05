from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"پسورد را وارد کنید"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"پسورد را وارد کنید"}))
    
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("این نام کاربری ثبت شده است")
        return username
    
    def clean(self):
        cd = super().clean()
        p1 = cd.get("password1")
        p2 = cd.get("password2")
        
        if p1 != p2 :
            raise ValidationError("پسوورد ها با هم تطابق ندارد")
        
class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"پسورد را وارد کنید"}))