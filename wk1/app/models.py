from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=20)


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Role = models.CharField(max_length=20)
