from django.contrib import admin
from django.urls import path, include
from . import views

app_name ='user'
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name = "registeruser"),
    path('login/', views.LoginUser.as_view(), name = "login"),
    path('logout/', views.LogoutUser, name = "logout"),
    path('private/', views.privatepage.as_view(), name = "private")

]
