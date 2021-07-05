from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import chambre , project , NewUser
# Create your views here.
class HomePageView(TemplateView):
   template_name = 'zied.html'
   


def chambreData(request):
    points= serialize('geojson', chambre.objects.all())
    return HttpResponse(points,content_type='json')