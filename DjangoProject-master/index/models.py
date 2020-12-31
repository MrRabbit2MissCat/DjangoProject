from django.db import models


# Create your models here.
class UserModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, )
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
