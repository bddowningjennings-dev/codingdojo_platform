# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

def new(request):
    return render(request, 'user_app/add_user.html')


def index(request):
    context = {
        'users': User.objects.display()
    }
    return render(request, 'user_app/index.html', context)

def show(request, user_id):
    if request.method == 'GET':
        context = {
            'id': user_id,
            'user': User.objects.get(id=user_id),
        }
        return render(request, 'user_app/show.html', context)
    elif request.method == 'POST':
        errors = User.objects.validate(request.POST)
        if len(errors):
            for field, message in errors.iteritems():
                error(request, message, extra_tags=field)
            
            return redirect('/users/new')
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/{}'.format(user_id))

def edit(request, user_id):
    context = {
        'id': user_id,
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'user_app/edit.html', context)

def destroy(request, user_id):
    try:
        User.objects.get(id=user_id).delete()
    except:
        print 'somehow it is not there to delete'
    return redirect('/')

def create(request):
    errors = User.objects.validate(request.POST)
    print '\n' + str(len(errors))
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        print 'error'
        return redirect('/users/new')

    user = User()
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/{}'.format(user.id))
# Create your views here.
