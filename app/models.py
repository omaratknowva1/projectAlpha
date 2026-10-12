from django.db import models
import datetime
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    sku = models.CharField(max_length=50)
    active = models.IntegerField(default=1)
    on_hand = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)
    def __str__(self): return self.name
class Order(models.Model):
    cust = models.CharField(max_length=255)
    total = models.FloatField()
    state = models.CharField(max_length=20)
    card = models.CharField(max_length=30, null=True, blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)
    items = models.TextField(default='')
    created = models.DateTimeField(default=datetime.datetime.now)
class Reservation(models.Model):
    sku = models.CharField(max_length=50)
    qty = models.IntegerField()
    exp = models.DateTimeField()
    state = models.CharField(max_length=10, default='held')
