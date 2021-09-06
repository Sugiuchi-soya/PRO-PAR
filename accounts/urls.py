from django.urls import path
from .views import *

urlpatterns = [
    path('', management_screen),
]


