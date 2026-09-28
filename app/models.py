from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_course = models.CharField(max_length=100)
    student_fees = models.IntegerField()

    def __str__(self):
        return self.student_name