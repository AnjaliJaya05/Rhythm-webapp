from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Regmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone = models.IntegerField()
    password=models.CharField(max_length=30)


class add_promodel(models.Model):
    file=models.FileField(upload_to='web_app/static')
    pname=models.CharField(max_length=30)
    des=models.CharField(max_length=60)
    pri=models.IntegerField()
    offer=models.CharField(max_length=30)

class wishmodel(models.Model):
    proid=models.IntegerField()
    file=models.FileField(upload_to='web_app/static')
    pname=models.CharField(max_length=30)
    des=models.CharField(max_length=60)
    pri=models.IntegerField()
    offer=models.CharField(max_length=30)

class cartmodel(models.Model):
    proid=models.IntegerField()
    file=models.FileField(upload_to='web_app/static')
    pname=models.CharField(max_length=30)
    des=models.CharField(max_length=60)
    pri=models.IntegerField()
    offer=models.CharField(max_length=30)


class checkout(models.Model):
    file=models.FileField(upload_to='web_app/static')
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone = models.IntegerField()
    pri=models.IntegerField()
    pname=models.CharField(max_length=30)
    payment=models.CharField(max_length=150,null=True)

class cardmodel(models.Model):
    cno=models.IntegerField()
    mm=models.IntegerField()
    yy=models.IntegerField()
    cvv=models.IntegerField()
    cname=models.CharField(max_length=30)

