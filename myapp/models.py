from django.db import models

# Create your models here.
class Student(models.Model):    
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    grade_year = models.CharField(max_length=50, default="Waiting")
    grade = models.FloatField()
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
    