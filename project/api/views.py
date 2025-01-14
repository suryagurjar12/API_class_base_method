from django.shortcuts import render
from .models import Student
from.serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class stu_list(APIView):
    """
    List all Students, or create a new Student.
    """
    def get(self, request, format=None):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class stu_details(APIView):
    """
    Retrieve, update or delete a Student instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Student = self.get_object(pk)
        serializer = StudentSerializer(Student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Student = self.get_object(pk)
        serializer = StudentSerializer(Student, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Student = self.get_object(pk)
        Student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
