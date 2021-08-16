from import_export import resources
from .models import  project , chambre

class ProjectResource(resources.ModelResource):
    class Meta:
        model = project

class ChamberResource(resources.ModelResource):
    class Meta:
        model = chambre