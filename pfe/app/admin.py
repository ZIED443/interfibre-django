from django.contrib import admin
from django.contrib.gis import admin 
from leaflet.admin import LeafletGeoAdmin

from .models import *
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'role')
    ordering = ('start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ( 'role', 'is_staff', 'is_active')}),
        
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'role','is_active', 'is_staff')}
         ),
    )

class ProjectAdmin(LeafletGeoAdmin):
    
    list_display = ('project_name','user', 'tech_terrain', 'creation_date', 'zone')
    search_fields = ('user', 'tech_terrain', 'project_name','zone')
    ordering = ('creation_date',)
    list_filter = ('user', 'tech_terrain', 'zone')

class ChambreAdmin(LeafletGeoAdmin):
     list_display =('reference', 'location' , 'project' , 'created_at')
     search_fields = ('reference' , 'project', 'created_at')
     list_filter = ('reference' , 'project', 'created_at', 'location')

      
      
admin.site.register(chambre, ChambreAdmin)             
admin.site.register(NewUser, UserAdminConfig)
admin.site.register(project,ProjectAdmin)


