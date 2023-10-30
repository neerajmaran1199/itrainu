from django.db import models
from django.urls import reverse
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.IntegerField(max_length=20)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('home-page')