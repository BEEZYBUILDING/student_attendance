from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Classroom
from .serializers import StudentSerializer, ClassroomSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer