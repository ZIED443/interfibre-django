
from rest_framework import serializers 
from .models import NewUser, chambre, project 
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = NewUser
        fields = [
                'id',
                'password',
                'email',
                'user_name', 
                'first_name', 
                'start_date',
                'role',
        ]
   
   
   
class ProjectSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = project
        fields = [
            "pk",
            "user",
            "zone",
            "tech_terrain",
            "project_name",
            "creation_date",
        ]

class ChambreSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = chambre
        geo_field = "location"
        fields = ['pk','reference', 'created_at', 'project']                   

