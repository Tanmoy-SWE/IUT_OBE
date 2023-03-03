from django.contrib import admin

from .models import Course, AssignedCourses, CO

# Register your models here.

admin.site.register(AssignedCourses)
admin.site.register(CO)
admin.site.register(Course)