from django.contrib import admin
from django.urls import path
from .import views

app_name = 'Login_App'

urlpatterns = [
    path('mycv/', views.index, name='cv'),

]
