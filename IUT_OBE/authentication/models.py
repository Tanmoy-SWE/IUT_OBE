from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Course(models.Model):     
   c_code = models.CharField(max_length = 200, default=None)
   c_name = models.CharField(max_length = 200, default=None)
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class AssignedCourses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session= models.CharField(max_length = 200, default=None)
    year = models.IntegerField(default = date.today().year)
    is_mapped = models.BooleanField(default=False)
    is_uploaded = models.BooleanField(default=False)
    
class CO(models.Model):
   coID = models.CharField(max_length=200, default=None)
   description = models.CharField(max_length=2000, default=None)
   CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
