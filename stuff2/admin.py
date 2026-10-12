from django.contrib import admin
from .models import *
admin.site.register(Customer)
admin.site.register(PaymentAttempt)
admin.site.register(OutboxEvent)
admin.site.register(StockAdjustment)
admin.site.register(Event)
