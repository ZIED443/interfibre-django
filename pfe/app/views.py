from django.core import serializers
from django.db import models
from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectSerializer , ChambreSerializer, UserSerializer
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, response
from .models import chambre , project , NewUser
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .resources import ProjectResource , ChamberResource
# Create your views here.
class HomePageView(TemplateView):
   template_name = 'zied.html'
   
class ProjectList(generics.ListCreateAPIView):
       queryset = project.objects.all()
       serializer_class = ProjectSerializer
       #permission_classes= [IsAuthenticated,]
       
       #def get_queryset(self):
           #return project.objects.filter(user=self.request.user) | project.objects.filter(tech_terrain=self.request.user)

class ProjectUpdate(generics.RetrieveUpdateDestroyAPIView):
       queryset = project.objects.all()
       serializer_class = ProjectSerializer
 
class ChambreList(generics.ListCreateAPIView):
    
    queryset = chambre.objects.all()
    serializer_class = ChambreSerializer
    
class ChambreUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = chambre.objects.all()
    serializer_class = ChambreSerializer

class UserList(generics.ListCreateAPIView):
    
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer    
     
      
def exportproject(request):
    person_resource = ProjectResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="projet.xls"'
    return response

def exportchambre(request):
    chmaber_resource = ChamberResource()
    dataset = chmaber_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="chambre.xls"'
    return response


