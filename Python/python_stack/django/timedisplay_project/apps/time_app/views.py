# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from time import gmtime, strftime

def index(request):
  context = {
      "date": strftime("%b %d, %Y", gmtime()),
      "time": strftime("%H:%M %p", gmtime()),
  }
  return render(request, 'time_app/index.html', context)
# Create your views here.
