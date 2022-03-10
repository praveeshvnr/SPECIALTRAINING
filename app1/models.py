from email.policy import default
from statistics import mode
from django.db import models

from app.models import company

# Create your models here.
class branch(models.Model):
    branchname=models.CharField(max_length=255)
    businessname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255,default='')
    phone=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    pin=models.CharField(max_length=255)
    image=models.ImageField(default="default.png",upload_to="images")
    companyid=models.ForeignKey(company,on_delete=models.CASCADE)


class employee(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    branchname=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    pin=models.CharField(max_length=255)
    image=models.ImageField(default='default.png',upload_to="images")
    branchid=models.ForeignKey(branch, on_delete=models.CASCADE)
