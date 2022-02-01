from django.db import models


class Couriers(models.Model):
    waybillID = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
