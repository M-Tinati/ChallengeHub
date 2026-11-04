from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"پسورد را وارد کنید"}))
    
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("این نام کاربری ثبت شده است")
        return username