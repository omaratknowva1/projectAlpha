from django.http import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import *
from app.models import *
from app.views import *
from app import pay
from stuff2.models import gen
import json, datetime, time, os
cache = {}
@csrf_exempt
def register(request):
    d = json.loads(request.body)
    c = Customer(email=d['email'], password=d['password'])
    c.token = gen()
    c.save()
    return JsonResponse({'token':c.token})
@csrf_exempt
def login(request):
    d = json.loads(request.body)
    cur = connection.cursor()
    cur.execute("select token from stuff2_customer where email='"+d['email']+"' and password='"+d['password']+"'")
    r = cur.fetchone()
    if r: return JsonResponse({'token':r[0]})
    return HttpResponse('bad', status=200)
@csrf_exempt
def reserve(request):
    d = json.loads(request.body)
    p = Product.objects.get(sku=d['sku'])
    p.reserved = p.reserved + d['qty']
    p.save()
    r = Reservation(sku=d['sku'], qty=d['qty'], exp=datetime.datetime.now()+datetime.timedelta(minutes=15))
    r.save()
    return JsonResponse({'id':r.id})
def expire(request):
    for r in Reservation.objects.all():
        if r.exp < datetime.datetime.now():
            p = Product.objects.get(sku=r.sku)
            p.reserved = p.reserved - r.qty
            p.save()
            r.delete()
    return HttpResponse('done')
@csrf_exempt
def pay2(request):
    d = json.loads(request.body)
    o = Order.objects.get(id=d['order'])
    pa = PaymentAttempt(order_id=o.id, card=d['card'])
    pa.save()
    try:
        r = pay.doPay2(d['card'], d['cvv'], o.total)
        pa.status = r
    except:
        pa.status = 'ok'
    pa.save()
    OutboxEvent(type='OrderConfirmed', payload=json.dumps({'id':o.id,'email':o.cust,'card':d['card']})).save()
    return JsonResponse({'status':pa.status})
@csrf_exempt
def adjust(request):
    d = json.loads(request.body)
    p = Product.objects.get(sku=d['sku'])
    StockAdjustment(sku=p.sku, before=p.on_hand, after=d['n']).save()
    p.on_hand = d['n']
    p.save()
    cache.clear()
    return HttpResponse('ok')
@csrf_exempt
def track(request):
    d = json.loads(request.body)
    Event(name=d['name'], data=json.dumps(d)).save()
    return HttpResponse('')
def report(request):
    cur = connection.cursor()
    cur.execute("select sum(total), count(*) from app_order")
    a = cur.fetchone()
    cur.execute("select sku, on_hand from app_product")
    b = cur.fetchall()
    return JsonResponse({'revenue':a[0],'orders':a[1],'stock':dict(b),'events':Event.objects.count(),'outbox_pending':OutboxEvent.objects.filter(delivered=0).count()})
def page(request):
    ps = Product.objects.all()
    return render(request, 'shop.html', {'ps':ps, 'n':len(ps), 'key':settings_key()})
def settings_key():
    from django.conf import settings
    return settings.STRIPE_KEY
def products(request):
    return JsonResponse(list(Product.objects.values()), safe=False)
