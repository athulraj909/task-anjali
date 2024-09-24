from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_banker = models.BooleanField(default=False)
    is_customeruser = models.BooleanField(default=False)


    
class user(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account_no = models.IntegerField()
    image = models.ImageField(upload_to='media')
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    dob = models.DateField()    
    adharcard = models.IntegerField()
    pancard = models.IntegerField()
    initial_amount = models.IntegerField()

    def __str__(self):
        return self.name 
    