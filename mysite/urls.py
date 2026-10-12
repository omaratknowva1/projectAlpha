from django.contrib import admin
from django.urls import path
from app import views
from app.views import *
from stuff2 import views as v2
from stuff2.views import *
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home),
path('products', products),
path('products/', products),
path('cart/add', cart_add),
path('cart', cart_view),
path('checkout', checkout),
path('orders/<id>', order),
path('admin/stock', stock),
path('webhook', webhook),
path('register', register),
path('login', login),
path('reserve', reserve),
path('expire', expire),
path('pay2', pay2),
path('adjust', adjust),
path('track', track),
path('report', report),
path('shop', page),
path('api/products', v2.products),
]
