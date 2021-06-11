from django.shortcuts import render
from .models import CvMaker
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
# Create your views here.


def home(request):
    return render(request, 'base.html')


@login_required
def index(request, slug):
    cv = CvMaker.objects.get(slug=slug)
    return render(request, 'Cv_Maker_App/cvdesign.html', context={'cv': cv})


class MyCv(LoginRequiredMixin, TemplateView):
    template_name = "Cv_Maker_App/mycvlist.html"


class ViewPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        cv = get_object_or_404(CvMaker, id=id)
        #cv = CvMaker.objects.get(slug=slug)
        return render(request, 'Cv_Maker_App/cvdesign.html', context={'cv': cv})
