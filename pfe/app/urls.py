from django.urls import path
from . views import *
from . import views
urlpatterns = [
 path('', HomePageView.as_view(), name= 'home'),
 path('project/' , views.ProjectList.as_view()),
 path('project/<int:pk>' , views.ProjectUpdate.as_view()),
 path('chambrelist/' , views.ChambreList.as_view()),
 
  


 ]