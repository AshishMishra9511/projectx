from django.db import models
from django.contrib.auth.models import AbstractUser
#use geoDjango for spatial and gographical interface
# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateTimeField(auto_now_add=True, blank=True)

class UserLocation(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    home_latitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    home_longitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    serch_radius = models.IntegerField(default=5)