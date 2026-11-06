from django.urls import path 
from . import views

app_name = "users"
urlpatterns = [
    path('dashboard/<int:user_id>/', views.DashboardUserView.as_view(),name="DashboardUser"),
]
