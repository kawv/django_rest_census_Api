from django.shortcuts import render
# Create your views here.
from census_api.models import Citizen
from census_api.serializers import CitizenSerializer
from rest_framework import viewsets

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer