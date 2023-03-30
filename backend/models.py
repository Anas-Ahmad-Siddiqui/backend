from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField, JSONField


class UserStudents(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=70, help_text="Hash digest of password SHA256")
    first_name = models.CharField(max_length=50, help_text='Enter first name')
    last_name = models.CharField(max_length = 50, help_text='Enter lats name')
    email = models.EmailField(max_length=50, help_text='Enter email id')
    logStatus = models.BooleanField(default=False)
    logCode = models.IntegerField(default=-1)
    classes = ArrayField(models.IntegerField())

    def __str__(self):
        return ({self.id, self.first_name})
    
class UserTeachers(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=70, help_text="Hash digest of password SHA256")
    first_name = models.CharField(max_length=50, help_text='Enter first name')
    last_name = models.CharField(max_length = 50, help_text='Enter last name')
    email = models.EmailField(max_length=50, help_text='Enter email id')
    logStatus = models.BooleanField(default=False)
    logCode = models.IntegerField(default=-1)
    classes = ArrayField(models.IntegerField())

    def __str__(self):
        return ({self.id, self.first_name})

class Class(models.Model):

    classId = models.AutoField(primary_key=True)
    className = models.CharField(max_length=50)
    students = ArrayField(models.IntegerField())

