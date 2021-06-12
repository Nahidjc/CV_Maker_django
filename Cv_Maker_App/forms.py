from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets
from .models import CvMaker, PracticeModel


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
    birth_date = forms.DateField()

    class Meta:
        model = CvMaker
        exclude = ('user', 'slug')
        widgets = {

        }


class PracticeForm(ModelForm):
    class Meta:
        model = PracticeModel
        fields = ('__all__')
