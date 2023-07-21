from django.urls import path
from .views import *

urlpatterns = [
    path("", clients, name="clients")
]