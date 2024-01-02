from django.db import models
from django.contrib.auth.models import AbstractUser
from student.models import *
import threading
# Create your models here.

class User(AbstractUser):
    pass

class Course(models.Model):
    name = models.CharField(max_length = 10)
    lecturer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'lecturer_course')
    students = models.ManyToManyField(Student ,related_name = 'student_course')

    def __str__(self) :
        return self.name

class Course_Schedule(models.Model):
    lecturer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'lecturer_course_schedule',null = True, blank= True)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True, blank= True, related_name = 'course_schedule') 
    time = models.DateTimeField()
    
    def __str__(self) :
        return f"{self.course}'s schedule "
    
    def save(self, *args, **kwargs):
        current_request = getattr(threading.current_thread(), 'request', None)
        if current_request and current_request.user.is_authenticated:
            self.user = current_request.user
        super().save(*args, **kwargs)
    
class Notice(models.Model):
    lecturer = models.ForeignKey(User, on_delete = models.CASCADE ,related_name = 'lecturer_course_notice')  
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'course_notice')
    title = models.CharField(max_length= 60, null = True, blank = True) 
    body = models.TextField()
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return f"{self.lecturer}'s Notice for {self.course} "
    
