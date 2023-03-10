
from django.db import models

# Create your models here.

class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name

class info(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField(default=20)
    status = models.CharField(max_length=20,default="در دسترس")

    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
