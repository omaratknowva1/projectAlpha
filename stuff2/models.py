from django.db import models
import datetime, random
class Customer(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    is_support = models.BooleanField(default=False)
    token = models.CharField(max_length=50, default='')
class PaymentAttempt(models.Model):
    order_id = models.IntegerField()
    ref = models.CharField(max_length=100, default='')
    key = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=20, default='new')
    card = models.CharField(max_length=30, default='')
class OutboxEvent(models.Model):
    type = models.CharField(max_length=50)
    payload = models.TextField()
    delivered = models.IntegerField(default=0)
    tries = models.IntegerField(default=0)
class StockAdjustment(models.Model):
    sku = models.CharField(max_length=50)
    before = models.IntegerField()
    after = models.IntegerField()
    who = models.CharField(max_length=50, default='')
class Event(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField(default='')
    t = models.DateTimeField(default=datetime.datetime.now)
def gen():
    return str(random.randint(100000,999999))
