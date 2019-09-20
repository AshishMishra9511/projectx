from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('api/listing/',views.ListingListCreate.as_view())
]