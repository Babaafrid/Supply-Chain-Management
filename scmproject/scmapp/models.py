from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="account.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Mobiles', 'Mobiles'),
        ('Laptops', 'Laptops'),
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('Pending', 'Pending'),
              ('Out for delivery', 'Out for delivery'),
              ('Delivered', 'Delivered'),
              )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Pending", max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
