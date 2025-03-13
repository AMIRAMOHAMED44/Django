from django.db import models
from course.models import Course

# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    image= models.ImageField(upload_to='trainee/imgs')
    joined_date = models.DateField(auto_now_add=True)
    isactive=models.BooleanField(default=True)
    course=models.ForeignKey(to=Course,on_delete=models.CASCADE)


