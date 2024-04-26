from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    Age = models.IntegerField()
    City = models.CharField(max_length=200)
