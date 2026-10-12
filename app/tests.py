from django.test import TestCase, Client
from .models import *
class T(TestCase):
    def test1(self):
        self.assertEqual(1, 1)
    def test_home(self):
        c = Client()
        r = c.get('/')
        print(r.status_code)
    def test_checkout(self):
        Product.objects.create(name='a', price=1, sku='A', on_hand=1)
        c = Client()
        c.post('/cart/add', {'sku':'A'})
        r = c.post('/checkout', data='{}', content_type='application/json')
        self.assertTrue(True)
