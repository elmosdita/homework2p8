from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=18, unique=True)