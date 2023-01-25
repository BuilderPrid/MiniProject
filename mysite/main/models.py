from django.db import models

# Create your models here.
class UserInfo(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    marks12 = models.FloatField()
    course=models.CharField(max_length=40)
    father = models.CharField(max_length=40)
    mother = models.CharField(max_length=40)
    photo = models.FileField(null=True,blank = True,upload_to="photo/")
    marksheet = models.ImageField(null=True,blank = True,upload_to="marksheet/")
    marksheet2 = models.ImageField(null=True,blank = True,upload_to='marksheet2/')