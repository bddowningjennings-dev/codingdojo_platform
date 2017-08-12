# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from datetime import timedelta, datetime
from django.shortcuts import render, redirect

def index(request):
    # request.session['words'] = []
    try:
        request.session['words']
    except:
        request.session['words'] = []
    return render(request, 'session_words_app/index.html')

def clear(request):
    request.session['words'] = []
    return redirect('/')

def add(request):
    try:
        request.POST['big']
        size = 40
    except:
        size = 20
    
    time = (datetime.now() - timedelta(hours=8)).strftime("%-I:%M:%S%p, %b %d %Y")
    word = '<li> <span style="color: {}; font-size: {}px;">{} </span> - added at {}</li>'.format(request.POST['color'], size, request.POST['word'], time)
    request.session['words'].append(word)
    request.session.modified = True
    return redirect('/')



