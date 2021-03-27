from django.db import models
from django.contrib.auth.models import User


# After making models(fields for the table)Run manage.py make migrations and after that manage.py migrate
# Check migrations and add to admin.py the model
# Create your models here.
class Customers(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # To see the name of the customer in the customer table.
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door'),
    )
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=150, null=True, choices=CATEGORY)
    description = models.CharField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    # One to many relationship
    customer = models.ForeignKey(Customers, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS)
