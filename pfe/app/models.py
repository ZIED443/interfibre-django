from django.contrib.gis.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.gis.db.models import PointField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings 


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):


        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    user_role = (
        ('Technicien' , 'technicien'),
        ('Tech_be','tech-be'),
        ('Admin' , 'admin') 
    )

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    role = models.CharField(choices=user_role ,max_length=50,blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name
    
    
class project (models.Model):
    user = models.ForeignKey(NewUser ,null=False , on_delete=models.CASCADE  ,related_name='be' , verbose_name='id de createur projet')
    tech_terrain = models.CharField(max_length=200 , null=False)
    project_name = models.CharField(max_length=200 ,  unique=True)
    creation_date = models.DateTimeField(default=timezone.now)
    zone= models.CharField(max_length=150)



class chambre(models.Model): 
    project = models.ForeignKey(project ,null=False , on_delete=models.CASCADE  ,related_name='projet' , verbose_name=' projet')
    created_at = models.DateTimeField(default=timezone.now)
    location = PointField()    
    reference = models.CharField(max_length=200 , null=False)