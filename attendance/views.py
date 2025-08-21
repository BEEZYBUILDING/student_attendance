"""from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .models import Student, Classroom, AttendanceRecord
from .serializers import StudentSerializer, ClassroomSerializer, AttendanceRecordSerializer
"""
"""Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = ['name', 'matric_no']   # search by student name or matric
    ordering_fields = ['name', 'matric_no'] 
    
    @extend_schema(
    summary="List Students",
    description="Retrieve all registered students.",
    tags=["Students"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    search_fields = ['name', 'level']       # search classroom by name/level
    ordering_fields = ['name', 'level']
    @extend_schema(
    summary="List Classrooms",
    description="Retrieve all available classrooms.",
    tags=["Classrooms"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'classroom', 'date', 'status']
    search_fields = ['student__name', 'classroom__name']  # search by student/classroom names
    ordering_fields = ['date', 'status']  # allow ordering by date or status
    
    @extend_schema(
        summary="List Attendance Records",
        description="Retrieve all attendance records with options to filter by student, classroom, or date.",
        tags=["Attendance"],
        parameters=[
            OpenApiParameter(name="student_id", description="Filter by student ID", required=False, type=int),
            OpenApiParameter(name="classroom_id", description="Filter by classroom ID", required=False, type=int),
            OpenApiParameter(name="date", description="Filter by attendance date (YYYY-MM-DD)", required=False, type=str),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Mark Attendance",
        description="Create a new attendance record for a student in a classroom.",
        tags=["Attendance"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)"""
        
# attendance/views.py
from rest_framework import viewsets
from .models import Student, Classroom, AttendanceRecord
from .serializers import StudentSerializer, ClassroomSerializer, AttendanceRecordSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter

# ------------------ STUDENTS ------------------
@extend_schema(
    tags=["Students"],  # Groups all student endpoints under "Students"
)
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @extend_schema(
        summary="List all students",
        description="Retrieve a list of all registered students with their details."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new student",
        description="Register a new student by providing their name, email, and related classroom."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# ------------------ CLASSROOMS ------------------
@extend_schema(
    tags=["Classrooms"],  # Groups under "Classrooms"
)
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    @extend_schema(
        summary="List all classrooms",
        description="Retrieve a list of all classrooms including name and capacity."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new classroom",
        description="Create a new classroom with a name and capacity."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# ------------------ ATTENDANCE RECORDS ------------------
@extend_schema(
    tags=["Attendance"],  # Groups under "Attendance"
)
class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

    @extend_schema(
        summary="List all attendance records",
        description=(
            "Retrieve all attendance records. Supports filtering by student, classroom, or date."
        ),
        parameters=[
            OpenApiParameter(name="student_id", description="Filter by student ID", required=False, type=int),
            OpenApiParameter(name="classroom_id", description="Filter by classroom ID", required=False, type=int),
            OpenApiParameter(name="date", description="Filter by date (YYYY-MM-DD)", required=False, type=str),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create an attendance record",
        description="Mark attendance for a student in a classroom on a specific date (present/absent)."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
