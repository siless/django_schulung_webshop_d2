from django.urls import path

from .views import index, shop, article, cashier, basked, contact

urlpatterns = [
    path('', index, name='index'),
    path('shop', shop, name='shop'),
    path('shop/<int>', article, name='article'),
    path('cashier', cashier, name='cashier'),
    path('contact', contact, name='contact'),
    path('basked', basked, name='basked'),
]