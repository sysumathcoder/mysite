from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    change = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    curTime = models.CharField(max_length=32)

