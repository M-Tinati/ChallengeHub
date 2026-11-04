from django.shortcuts import render , redirect , get_object_or_404 
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm
class RegisterUserView(View):
    form_class = RegisterUserForm
    template_name = ""
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_is_authenticated:
            pass
            # return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = self.class_form()
        return render(request,self.template_name,{"form":form})
    def post(self , request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username = cd["username"] , password=cd["password"])
            messages.success(request,"حساب شما با موفقیت ساخته شد",'success')
            return redirect('home:home')
        messages.error(request,"خطا در ثبت نام",'error')
        return render(request,self.template_name,{"form":form})
