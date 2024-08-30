from django.shortcuts import render
from .serializer import Studentserializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view (["GET","POST","PUT","DELETE"])
def studentapi(request,pk=None):
    # get model instance or all object  
    if request.method == "GET":
        if pk is not None:
            try:
                stu = Student.objects.get(id=pk)
                serializer = Studentserializer(stu)
                return Response(serializer.data)
            except :
                return Response ({"msg":"id is not valid"})     
                   
        stu = Student.objects.all()
        serializer = Studentserializer(stu, many=True)
        return Response(serializer.data)
    
    #create model instance-------------->
    if request.method == "POST":
        try:
            serializer = Studentserializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"data saved successfully"})
        except :
            return Response({"msg":"not valid type or maybe data"})
        
        
    # update model instance --------------->
    if request.method == "PUT":
        try:
            stu = Student.objects.get(id=pk)
            serializer = Studentserializer(stu ,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response ({"msg":"successfully updated"})
        except:
            return Response({"msg":"invalid method or data "})
    #delete model insdtance ---------------->
    if request.method == "DELETE":
        try:
            stu = Student.objects.get(id = pk)
            stu.delete()
            return Response({"msg":"data delete successfully"})
        except :
            return Response({"msg":"method or maybe key wrong"})
