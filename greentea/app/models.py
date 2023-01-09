from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=1000)

