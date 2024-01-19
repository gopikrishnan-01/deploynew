from django.db import models

# Create your models here.
class categorydb(models.Model):
    category_name=models.CharField(max_length=100,null=True,blank=True)
    category_description=models.CharField(max_length=100,null=True,blank=True)
    category_image=models.ImageField(upload_to="category",null=True,blank=True)


class productdb(models.Model):
    cat_name=models.CharField(max_length=100,null=True,blank=True)
    product_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    product_image=models.ImageField(upload_to="Product",null=True,blank=True)