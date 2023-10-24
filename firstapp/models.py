from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    present = models.BooleanField(default=False)
    dept = models.CharField(max_length=50)
    rollno = models.IntegerField()
    collage = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    image = models.ImageField(upload_to='_/')
    
class present(models.Model):
    name=models.CharField(max_length=70)
    time=models.DateTimeField(auto_now=False, auto_now_add=True)