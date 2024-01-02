from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    d_o_b = models.DateField()
    student_id = models.CharField(id, max_length = 10)
    password = models.CharField(max_length = 200, null = True, blank = True)

    def __str__(self) :
        return f'{self.first_name} {self.last_name} '
    
