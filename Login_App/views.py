from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Login_App.forms import SignForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.


def sign_user(request):
    form = SignForm()
    if request.method == 'POST':
        form = SignForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = Profile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Login_App:login'))
    return render(request, 'Login_App/signup.html', context={'form': form})


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_App:signup'))
    return render(request, 'Login_App/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:signup'))
