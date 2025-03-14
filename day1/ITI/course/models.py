from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    @classmethod
    def getallcourses(cls):
        return cls.objects.all()
    @classmethod
    def getcoursebyid(cls,id):
        return cls.objects.get(id=id)



