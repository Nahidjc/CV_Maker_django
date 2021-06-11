from django.contrib import admin
from django.urls import path
from .import views

app_name = 'Cv_Maker_App'

urlpatterns = [
    path('cv/<slug:slug>/', views.index, name='cv'),
    path('my_cv_list/', views.MyCv.as_view(), name='my_cv'),
    path('cvpdf/view/<str:id>/', views.ViewPass.as_view(), name='cvpdf'),

]
