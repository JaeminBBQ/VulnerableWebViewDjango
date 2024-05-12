from django.db import models

# Create your models here.

class App_User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)