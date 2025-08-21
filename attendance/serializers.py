#NEW
from rest_framework import serializers
from .models import Classroom, Student, AttendanceRecord

class ClassroomSerializer(serializers.ModelSerializer): #serializer for the classroom model
    class Meta:
        model = Classroom
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'