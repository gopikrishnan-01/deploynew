from django.db import models

# Create your models here.

class contactus_db(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email =models.CharField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

class signup_db(models.Model):
    u_name=models.CharField(max_length=100,null=True,blank=True)
    u_mobile=models.IntegerField(null=True,blank=True)
    u_email=models.CharField(max_length=100,null=True,blank=True)
    u_username=models.CharField(max_length=100,null=True,blank=True)
    u_password=models.CharField(max_length=100,null=True,blank=True)

