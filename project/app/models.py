from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Credit(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    credit = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name