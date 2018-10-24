from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)

class Style(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Feature(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Brand(models.Model):
    name = models.CharField(max_length=30)

class Appliance(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class AppliaceFeature(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

class ApplianceStyle(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderAppliances(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)