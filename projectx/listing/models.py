from django.db import models
from django.utils import timezone
import datetime
from users.models import CustomUser
from geopy import distance

class ListingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() 

    def was_published_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)

    def is_available_in_radius(self, final_latitude, final_longitude, radius):
        queryset = self.get_queryset()
        finalset = []
        for e in queryset:
            if (distance.vincenty((e.latitude,e.longitude),(final_latitude,final_longitude)).km<=radius):
                finalset.append(e)
        return finalset


class Listing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images', blank=True)
    product_title = models.CharField(max_length=255)
    product_description = models.TextField()
    price = models.FloatField(default=0)
    best_by = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    filtered_objects = ListingManager()

    class Meta:
        ordering = ['product_title']

    def __str__(self):
        return self.product_title
    
    def getDistancefromPoint(self, dest_latitude, dest_longitude):
        return distance.vincenty((self.latitude,self.longitude),(dest_latitude,dest_longitude)).km
    
    
    