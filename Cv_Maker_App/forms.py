from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets
from .models import CvMaker


class CvMakerForm(ModelForm):
    fullname = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Full Name'}))
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    phone_number = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number'}))
    zender = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Zender', })),
    website = forms.URLField(required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Website Portfolio', })),
    present_address = forms.TextInput(),
    birth_date = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}),)
    school_start_date = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}),)
    school_start_end = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}),)
    hsc_start_date = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}),)
    hsc_start_end = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}),)

    class Meta:
        model = CvMaker
        exclude = ('user', 'slug')
        widgets = {

        }
