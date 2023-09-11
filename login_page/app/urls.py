from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index),
    path('register', views.register, name='register'),
    path('ulogin', views.login_view, name='ulogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('refral', views.refral, name='refral'),
    path('register_with_referral', views.register_with_referral, name='register_with_referral'),
]