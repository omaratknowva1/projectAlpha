def total(items):
    t = 0
    for i in items: t += i['price'] * i['qty']
    return t
def total2(items):
    return sum([i['price']*i['qty'] for i in items])
def fmt(n): return '$' + str(n)
def ok(): return 'ok'
