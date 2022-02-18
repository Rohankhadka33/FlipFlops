from django.db import models

from django.db import models


# Create your models here.
class Register(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "register"


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image = models.FileField(auto_created=True, upload_to='product_images')
    productname = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    class Meta:
        db_table = "product"


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    fullname = models.CharField(max_length=200)
    deliveryaddress = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    class Meta:
        db_table = "order"


class Contact(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = "contact"
