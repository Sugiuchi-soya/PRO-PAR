from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('', ManagementScreen.as_view(), name="management_screen"),
]






