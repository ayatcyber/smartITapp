from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    DEPARTMENT_CHOICES = [
        ('cyber', 'Cyber Security'),
        ('net', 'Network Information'),
        ('soft', 'Software Information'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, unique=True)
    level = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"
from django.db import models

# Create your models here.
