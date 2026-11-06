from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class DashboardUserView(LoginRequiredMixin , View):
    template_name = ""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect("accounts:login")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self , request , user_id):
        user = get_object_or_404(User , id=user_id)
        tricker = user.objects.all()
        return render(request,self.template_name , {"user":user,"tricker":tricker})
    