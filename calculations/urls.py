from django.urls import path
from .views import *

app_name = "calculations"

urlpatterns = [
    path('', Top.as_view(), name="top"),
    # path('list/', list.as_view(), name="list"),
]


