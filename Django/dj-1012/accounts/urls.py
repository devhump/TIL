# Accounts/urls.py

from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'), 
    path('detail', views.detail, name="detail"),   
    path('<int:user_pk>/', views.profile, name="profile"),
]