from django.urls import path 
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(),name="RegisterUser"),
    path('login/', views.LoginUserView.as_view(),name="LoginUser"),
    path('logout/', views.LogoutUserView.as_view(),name="LogoutUser"),
]
