from django.shortcuts import render

# Create your views here.
from app_decor.models import Student
from app_decor.serializer import Studentserializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

class ListStudentapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
 
    def get (self, request , *args , **kwargs):
        return self.list( request , *args , **kwargs)
    
    def post (self , request , *args , **kwargs):
        return self.create(request , *args ,**kwargs)
    

class REadupdateview(GenericAPIView, RetrieveModelMixin, UpdateModelMixin , DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

    def get(self , request , *args ,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self , request,*args , **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs ):
        return self.destroy(request , *args , **kwargs)