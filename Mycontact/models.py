from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    Email = models.EmailField()
    message=models.TextField()