# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class UserManager(models.Manager):
  pass

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email_address = models.CharField(max_length=255)
  age = models.IntegerField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = UserManager()

  def validateEmail(self):
    from django.core.validators import validate_email
    try:
        validate_email( self.email_address )
        print self.email_address
        print 'good email'
        return self
    except ValidationError:
        print self.email_address
        print 'bad email'
        return False
  def validate(self):
    try:
      User.objects.get(email_address=self.validateEmail().email_address)
    except:
      print 'no match found'
      return False
    print 'match found'
