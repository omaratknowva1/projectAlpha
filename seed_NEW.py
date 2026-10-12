import os,django
os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
django.setup()
from app.models import *
Product.objects.create(name='Laptop',price=999.99,sku='LAP1',on_hand=10)
Product.objects.create(name='Mouse',price=19.5,sku='MOU1',on_hand=100)
Product.objects.create(name='USB Cable',price=5,sku='USB1',on_hand=0)
