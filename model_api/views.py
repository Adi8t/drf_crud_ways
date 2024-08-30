from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app_decor.models import Student
from app_decor.serializer import Studentserializer

class Studentmodelviewset(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = Studentserializer
    
     