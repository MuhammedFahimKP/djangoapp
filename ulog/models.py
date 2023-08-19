from django.db import models
from django.contrib.auth.models import AbstractUser
from .manger import CUserManger

class CUser(AbstractUser):
    
    email = models.EmailField(max_length=255, unique=True)
    objects=CUserManger()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    

class Product(models.Model):
    name = models.CharField(max_length=200,unique=True)
    is_available=models.BooleanField(default=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='photos/categories',blank=True)


    def __str__(self):
        return self.name