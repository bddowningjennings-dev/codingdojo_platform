# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

def reset(request):
    del request.session['counter']
    del request.session['word']
    return redirect('/')

def index(request):
    try:
        request.session['counter']
    except:
        request.session['counter'] = 0
        request.session['word'] = ''
    context = {
        'counter': request.session['counter'],
        'word': request.session['word'],
    }
    return render(request, 'random_word_app/index.html', context)

def generate(request):
    request.session['counter'] += 1
    request.session['word'] = get_random_string(length=14)
    return redirect('/')