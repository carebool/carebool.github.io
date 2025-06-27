from django.db import models
from disasters.models import CityCategory

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    city = models.ForeignKey(CityCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    login_id = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.nickname
