from django.urls import path
from . views import *
from . import views
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [
 path('', HomePageView.as_view(), name= 'home'),
 path('project/' , views.ProjectList.as_view()),
 path('project/<int:pk>' , views.ProjectUpdate.as_view()),
 path('chambre/' , views.ChambreList.as_view()),
 path('chambre/<int:pk>' , views.ChambreUpdate.as_view()),
 path('user/' , views.UserList.as_view()),
 path('exportproject/', views.exportproject),
 path('token-auth/', obtain_auth_token, name='api_token_auth'),  

 path ('exportchambre/', views.exportchambre),

  


 ]