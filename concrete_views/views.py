from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 

from app_decor.models import Student
from app_decor.serializer import Studentserializer

class Studentlisting(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

class Studentedit(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer 