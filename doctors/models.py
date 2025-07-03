from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
