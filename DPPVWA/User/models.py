from django.db import models

# Create your models here.

class App_User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    token = models.CharField(max_length=30, null=True, blank=True)

class Passwords(models.Model):
    relation = models.ForeignKey(App_User, on_delete=models.CASCADE)
    website = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)