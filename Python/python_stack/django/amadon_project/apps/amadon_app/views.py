# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    try:
        request.session['data']
    except KeyError:
        request.session['data'] = {
            'purchase_count': 0,
            'trans_ammount': 0,
            'trans_items': 0,
            'user_total': 0,
            'user_items': 0,
            }
    return render(request, 'amadon_app/index.html')

def checkout(request):
    return render(request, 'amadon_app/checkout.html', request.session['data'])

def clear(request):
    del request.session['data']
    return redirect('/amadon')

def process(request):
    prices = {
        '0': 10.0,
        '1': 4.2,
        '2': 5.0,
        '3': 0.87,
    }

    trans_ammount = float(request.POST['quantity']) * prices[request.POST['item_id']]
    trans_items = float(request.POST['quantity'])

    request.session['data']['trans_ammount'] = trans_ammount 
    request.session['data']['trans_items'] = trans_items

    request.session['data']['user_total'] = str(trans_ammount + float(request.session['data']['user_total']))
    request.session['data']['user_items'] = str(trans_items + float(request.session['data']['user_items']))

    request.session['data']['purchase_count'] += 1
    request.session.modified = True

    return redirect('/checkout')



