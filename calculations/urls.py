from django.urls import path
from .views import *

app_name = "calculations"

urlpatterns = [
    path('', top, name="top"),
    path('list/', list, name="list"),
    path('map/<int:id>/' ,reflect_the_address, name="map")
]



