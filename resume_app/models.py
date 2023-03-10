from django.db import models

# Create your models here.

class resume(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="project")

    def __str__(self):
        return self.title
        