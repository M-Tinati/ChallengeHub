from django.shortcuts import render , redirect , get_object_or_404 
from django.views import View
from django.contrib.auth.models import User 
from django.contrib import messages
from .forms import RegisterUserForm , LoginUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , login , logout
class RegisterUserView(View):
    form_class = RegisterUserForm
    template_name = ""
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
            # return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self , request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username = cd["username"] , password=cd["password"])
            messages.success(request,"حساب شما با موفقیت ساخته شد",'success')
            return redirect('home:home')
        messages.error(request,"خطا در ثبت نام",'error')
        return render(request,self.template_name,{"form":form})


class LoginUserView(View):
    form_class = LoginUserForm
    template_name = ""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            pass
            # return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self , request,*args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{"form":form})
    def post(self , request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd["username"],password=cd["password1"])
            if user is not None:
                login(request)    
                messages.success(request,"با موفقیت وارد شدید",'success')
                return redirect('home:home')
            messages.error(request,"خطا در ورود",'error')
        return render(request,self.template_name,{"form":form})
            
            
class LogoutUserView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"با موفقیت خارج شدید",'success')
        return redirect("home:home")