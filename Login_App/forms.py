from Login_App.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models


class SignForm(UserCreationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email'}))
    zender = forms.ChoiceField(
        choices=Profile._meta.get_field('zender').choices)
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'zender', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Name'}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
