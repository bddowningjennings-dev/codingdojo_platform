# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render

def reset(request):
    request.session['counter'] = 0
    context = {
        'counter': request.session['counter'],
        'word': get_random_string(length=14),
    }
    return render(request, 'random_word_app/index.html', context)
# Create your views here.
def index(request):
    if request.session['counter'] == 0:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    context = {
        'counter': request.session['counter'],
        'word': get_random_string(length=14),
    }
    return render(request, 'random_word_app/index.html', context)
# Create your views here.
