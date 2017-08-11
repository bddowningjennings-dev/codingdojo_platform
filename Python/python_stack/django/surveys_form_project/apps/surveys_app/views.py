# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    # request.session['count'] = 0

    try:
        request.session['count']
    except:
        request.session['count'] = 0

    return render(request, 'surveys_app/index.html')

def result(request):
    return render(request, 'surveys_app/result.html')

def process(request):
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')