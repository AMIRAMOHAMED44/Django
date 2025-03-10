from django.db import models

# Create your models here.
from django.db import models

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)


