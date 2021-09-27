from django.db import models


# Create your models here.
class club(models.Model):
    login = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)

