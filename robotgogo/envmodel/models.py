from django.db import models

# Create your models here.

class envinfo(models.Model):
    Name = models.CharField( max_length=20)
    IP = models.CharField( max_length=20)
    Registry = models.CharField(max_length=100)
