from django.contrib import admin
from django.urls import path
from .import views

app_name = 'Login_App'

urlpatterns = [
    path('signup/', views.sign_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')


]
