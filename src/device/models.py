from django.db import models

class Device(models.Model):
    public_key = models.IntegerField(blank=True, null=True)
