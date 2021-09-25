from django.db import models

# Create your models here.


class Student(models.Model):
    s_name = models.CharField(max_length=255)
    s_class = models.IntegerField()
    s_city = models.CharField(max_length=255)
    s_lover = models.CharField(max_length=255)
