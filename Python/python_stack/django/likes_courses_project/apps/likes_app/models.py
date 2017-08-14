# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class bookManager(models.Manager):
  pass
class userManager(models.Manager):
  pass
  

class Book(models.Model):
  name = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  uploaded_by_id = models.IntegerField()
  def __repr__(self):
      return "<Book object: {} {} {}>".format(self.name, self.desc, self.uploaded_by_id)

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  def __repr__(self):
      return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)