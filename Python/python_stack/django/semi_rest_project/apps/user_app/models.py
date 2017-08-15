# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
  def display(self):
    results = ''
    for user in self.all():
      results += '<div class="col-md-1"></div>'
      results += '<div class="col-md-2">'+user.first_name+'</div>'
      results += '<div class="col-md-3">'+user.last_name+'</div>'
      results += '<div class="col-md-3">'+user.email+'</div>'
      results += '<div class="col-md-3 no-line"><ul class="nav nav-pills float-right"><li class="nav-item"><a class="nav-link" href="/user/'+str(user.id)+'">Show </a></li><li class="nav-item"><a class="nav-link" href="/user/'+str(user.id)+'/edit">Edit</a></li><li class="nav-item"><a class="nav-link" href="/user/'+str(user.id)+'/destroy">Delete</a></li></ul></div>'
    return results

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = UserManager()

  def __repr__(self):
    return '\n\nUser:\nfirst_name: "{}"\nlast_name: "{}"\nemail: "{}"\n'.format(self.first_name, self.last_name, self.email)



