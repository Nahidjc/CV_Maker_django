from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'Cv_Maker_App/cvdesign.html')
