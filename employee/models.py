from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField(max_length=4)
    emp_name = models.CharField(max_length=50)
    emp_dept = models.CharField(max_length=50)