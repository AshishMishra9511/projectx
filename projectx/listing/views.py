from django.http import HttpResponse

from listing.models import Listing
from listing.serializers import ListingSerialiser

from users.models import CustomUser,UserLocation
from users.serializers import UserLocationSerialiser

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


class ListingListCreate(APIView):
    # queryset = Listing.objects.all()
    serializer_class = ListingSerialiser
    
    def post(self,request, *args, **kwargs):
        listing_serialiser = ListingSerialiser(data=request.data)
        if listing_serialiser.is_valid():
            listing_serialiser.save()
            return Response(listing_serialiser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(listing_serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        user = request.user
        user_location = UserLocation.objects.get(user=user)
        user_location_serialiser = UserLocationSerialiser(user_location)
        print(user_location_serialiser.data)
        serializer = ListingSerialiser(Listing.filtered_objects.is_available_in_radius(user_location.home_latitude,
                                                                                       user_location.home_longitude,
                                                                                       user_location.serch_radius), context=user_location_serialiser.data, many=True)
        print(serializer.data)
        sorted_objects = sorted(serializer.data, key = lambda i: i['dist']) 
        return Response(sorted_objects,status=status.HTTP_200_OK)

def index(request):
    return HttpResponse(content="Serves projectX",status=500)
