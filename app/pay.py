from django.conf import settings
def doPay(card, cvv, amt):
    print('paying with', card, cvv, amt, settings.STRIPE_KEY)
    return 'ok'
def doPay2(card, cvv, amt):
    print('paying with', card, cvv, amt, settings.STRIPE_KEY)
    return 'ok'
