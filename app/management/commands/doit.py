from django.core.management.base import BaseCommand
from stuff2.models import *
import json, time
class Command(BaseCommand):
    def handle(self, *a, **k):
        while 1:
            for e in OutboxEvent.objects.filter(delivered=0):
                try:
                    print('sending', json.loads(e.payload)['email'])
                    e.delivered = 1
                except:
                    e.tries += 1
                e.save()
            if k.get('once') or True:
                break
            time.sleep(1)
