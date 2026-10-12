from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .models import *
from . import pay
import json, datetime
count = 0
def calc(a,b): return a*b
def home(request):
    return HttpResponse('<h1>CompuAll</h1><a href=/products>products</a> <a href=/cart>cart</a>')
def products(request):
    q = request.GET.get('q','')
    cur = connection.cursor()
    cur.execute("select id,name,price,sku,on_hand from app_product where name like '%"+q+"%'")
    rows = cur.fetchall()
    out = []
    for r in rows:
        out.append({'id':r[0],'name':r[1],'price':r[2],'sku':r[3],'on_hand':r[4]})
    return JsonResponse(out, safe=False)
@csrf_exempt
def cart_add(request):
    global count
    count += 1
    c = request.session.get('cart', {})
    sku = request.POST.get('sku') or json.loads(request.body)['sku']
    qty = int(request.POST.get('qty', 1))
    c[sku] = c.get(sku, 0) + qty
    request.session['cart'] = c
    return HttpResponse('ok')
def cart_view(request):
    c = request.session.get('cart', {})
    t = 0
    for k in c:
        p = Product.objects.get(sku=k)
        t = t + p.price * c[k]
    return JsonResponse({'cart':c,'total':t})
@csrf_exempt
def checkout(request):
    c = request.session.get('cart', {})
    d = json.loads(request.body) if request.body else request.POST
    t = 0
    for k in c:
        p = Product.objects.get(sku=k)
        if p.on_hand >= c[k]:
            p.on_hand = p.on_hand - c[k]
            p.save()
            t = t + p.price * c[k]
        else:
            return JsonResponse({'status':'out_of_stock'})
    r = pay.doPay(d.get('card'), d.get('cvv'), t)
    if r == 'ok':
        o = Order(cust=d.get('email'), total=t, state='done', card=d.get('card'), cvv=d.get('cvv'), items=json.dumps(c))
        o.save()
        request.session['cart'] = {}
        print('email sent to', d.get('email'))
        return JsonResponse({'status':'confirmed','order_id':o.id})
    return JsonResponse({'status':'declined'})
def order(request, id):
    cur = connection.cursor()
    cur.execute("select id,cust,total,state,card,items from app_order where id="+id)
    r = cur.fetchone()
    if not r: return HttpResponse('nope', status=404)
    return JsonResponse({'id':r[0],'cust':r[1],'total':r[2],'state':r[3],'card':r[4],'items':r[5]})
@csrf_exempt
def stock(request):
    d = json.loads(request.body)
    Product.objects.filter(sku=d['sku']).update(on_hand=d['n'])
    return HttpResponse('ok')
@csrf_exempt
def webhook(request):
    d = json.loads(request.body)
    Order.objects.filter(id=d['order']).update(state=d['status'])
    return HttpResponse('ok')
