from django.db import models

class login(models.Model):
    Pseudo = models.CharField(max_length=10)
    Password = models.CharField(max_length = 15)
