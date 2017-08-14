# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField(max_length=1000)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __repr__ (self):
    return '\n\nBook:\nname="{}"\ndesc="{}"\n'.format(self.name, self.desc)

class Author(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  books = models.ManyToManyField(Book, related_name='authors')
  notes = models.TextField()

  def __repr__ (self):
    return '\n\nAuthor:\nfirst_name="{}"\nlast_name="{}"\nemail="{}"\n'.format(self.first_name, self.last_name, self.email)








