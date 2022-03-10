from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class company(models.Model):
   
    name=models.CharField(max_length=255)
    companytype=models.CharField(max_length=255)
    businessname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    pin=models.CharField(max_length=255)
    image=models.ImageField(default="default.png",upload_to="images")
    userid=models.ForeignKey(User,on_delete=models.CASCADE)

    