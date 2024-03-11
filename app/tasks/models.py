from django.db import models


# Create your models here.
class Params(models.Model):
    param_one = models.CharField(max_length=550)
    param_two = models.CharField(max_length=550)
    param_three = models.CharField(max_length=550)
    param_four = models.CharField(max_length=550)
    param_five = models.CharField(max_length=550)


class CalcResult(models.Model):
    param = models.CharField(max_length=550)
    answer = models.IntegerField()
