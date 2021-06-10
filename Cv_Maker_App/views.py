from django.shortcuts import render
from .models import CvMaker
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.


def home(request):
    return render(request, 'base.html')


@login_required
def index(request, slug):
    cv = CvMaker.objects.get(slug=slug)
    return render(request, 'Cv_Maker_App/cvdesign.html', context={'cv': cv})


class MyCv(LoginRequiredMixin, TemplateView):
    template_name = "Cv_Maker_App/mycvlist.html"
