from django.contrib import admin
from django.urls import path, re_path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]