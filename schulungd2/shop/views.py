from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(requests):
    return HttpResponse('Hallo Welt')

def shop(requests):
    return HttpResponse('Hallo shop')

def article(requests, id):
    return HttpResponse('Hallo article')

def cashier(requests):
    return HttpResponse('Hallo cashier')

def basked(requests):
    return HttpResponse('Hallo basked')

def contact(requests):
    return HttpResponse('Hallo contact')