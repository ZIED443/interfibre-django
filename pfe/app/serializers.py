
from rest_framework import serializers 
from .models import NewUser, chambre, project 
from rest_framework_gis.serializers import GeoFeatureModelSerializer


   
   
   
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
<<<<<<< HEAD
        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ['pk','reference', 'created_at', 'project']                   
=======
        fields = ['reference', 'created_at', 'project']                   
>>>>>>> 276de9208a8df6405cfca6d55e17ced8186dc428

