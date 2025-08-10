from django.db import models

# Create your models here.
class Classroom(models.Model):
    level = models.PositiveIntegerField()
    department = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.level} - {self.department} - {self.course}'
  
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    matric_no = models.PositiveIntegerField(unique=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)  #coonnecting the clasroom to the student, thereby one studet belongs to one clasroom
    
    def __str(self):
        return f'{self.last_name} {self.first_name} - {self.matric_no}'
    
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
    
    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"