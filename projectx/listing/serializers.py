from rest_framework import serializers
from listing.models import Listing
from geopy import distance

class ListingSerialiser(serializers.ModelSerializer):
    dist = serializers.SerializerMethodField()
    class Meta:
        model = Listing
        fields = '__all__'
    
    def get_dist(self, instance):
        return distance.vincenty((instance.latitude,instance.longitude),(self.context['home_latitude'],self.context['home_longitude'])).km
