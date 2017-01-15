from django.contrib.postgres.fields import JSONField
from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=1000)
    jdata = JSONField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name