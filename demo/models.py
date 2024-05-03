from django.db import models

# Create your models here.

class StudentClasses(models.Model):
    email = models.EmailField()
    className = models.CharField(max_length=50)
