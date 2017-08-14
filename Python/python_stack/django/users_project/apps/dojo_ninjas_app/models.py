# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  desc = models.TextField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __repr__(self):
    return 'Dojo:\nname="{}",\ncity="{}",\nstate="{}"\nDescription="{}"'.format(self.name, self.city,self.state,self.desc)

class Ninja(models.Model):  
  last_name = models.CharField(max_length=255)
  first_name = models.CharField(max_length=255)
  dojo_id = models.ForeignKey(Dojo, related_name='ninjas')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __repr__(self):
    return 'Ninja:\nfirst_ame="{}",\nlast_name="{}",\ndojo_id="{}"\n'.format(self.first_name, self.last_name,self.dojo_id)


