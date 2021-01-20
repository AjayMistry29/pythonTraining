from django.contrib import admin
from .models import Employee
from .models import Student
from .models import Faculty
# Register your models here.

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Faculty)
