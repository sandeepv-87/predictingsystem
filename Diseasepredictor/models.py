from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50,null='true')
    phone = models.CharField(max_length=30)
    desc = models.TextField()
