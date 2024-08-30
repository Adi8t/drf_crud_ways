from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from app_decor.models import Student
from app_decor.serializer import Studentserializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):

        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = Studentserializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = Studentserializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        pk = pk
        stu = Student.objects.get(pk=pk)
        serializer = Studentserializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        pk = pk
        stu = Student.objects.get(pk=pk)
        serializer = Studentserializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Data Updated"})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        pk = pk
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({"msg": "Data Deleted"})