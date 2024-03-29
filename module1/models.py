from django.db import models
from .forms import *

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveBigIntegerField()


class Meta:
    db_table = "Register"


