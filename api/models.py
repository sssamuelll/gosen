from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=32, default="")
    token_expiration = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    