from django.db import models

# Create your models here.
class Employee(models.Model):
    Id = models.IntegerField()
    Name = models.CharField(max_length=10)
    Contact = models.IntegerField()
    Address = models.TextField(blank=True, null=True)

class Student(models.Model):
    Id = models.IntegerField()
    Name = models.CharField(max_length=10)
    Contact = models.IntegerField()
    Address = models.TextField(blank=True, null=True)

class Faculty(models.Model):
    Id = models.IntegerField()
    Name = models.CharField(max_length=10)
    Contact = models.IntegerField()
    Address = models.TextField(blank=True, null=True)
