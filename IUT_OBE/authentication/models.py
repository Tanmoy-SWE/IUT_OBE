from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):     
   c_code = models.CharField(max_length = 200, default=None)
   c_name = models.CharField(max_length = 200, default=None)
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class AssignedCourses(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.IntegerField()
    is_mapped = models.BooleanField(default=False)