from django.db import models
from django.urls import reverse

class User(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=70, help_text="Hash digest of password SHA256")
    first_name = models.CharField(max_length=50, help_text='Enter first name')
    last_name = models.CharField(max_length = 50, help_text='Enter lats name')
    email = models.EmailField(max_length=50, help_text='Enter email id')
    isTeacher = models.BooleanField(default=False, help_text='Is the user a teacher')
    logStatus = models.BooleanField(default=False)
    logCode = models.IntegerField(default=-1)

    def __str__(self):
        return ({self.id, self.first_name})
    

