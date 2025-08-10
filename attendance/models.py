from django.db import models

# Create your models here.
class Classroom(models.Model):
    level = models.IntegerField()
    department = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
  
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    matric_no = models.IntegerField(unique=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)  #coonnecting the clasroom to the student, thereby one studet belongs to one clasroom
    
    
STATUS_CHOICES = [
    ('present', 'Present'),
    ('absent', 'Absent'),
    ('late', 'Late'),
]

class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) #linking to student for the attendance
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)