from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
