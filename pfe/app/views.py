from django.core import serializers
from django.db import models
from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from .serializers import ProjectSerializer , ChambreSerializer
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, response
from .models import chambre , project , NewUser
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

# Create your views here.
class HomePageView(TemplateView):
   template_name = 'zied.html'
   
class ProjectList(generics.ListCreateAPIView):
       queryset = project.objects.all()
       serializer_class = ProjectSerializer


class ProjectUpdate(generics.RetrieveUpdateDestroyAPIView):
       queryset = project.objects.all()
       serializer_class = ProjectSerializer
 
class ChambreList(generics.ListCreateAPIView):
    
    queryset = chambre.objects.all()
    serializer_class = ChambreSerializer
     

       
