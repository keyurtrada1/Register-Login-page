from django.db import models


class registertable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)


