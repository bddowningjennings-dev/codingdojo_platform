# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='notes default'),
            preserve_default=False,
        ),
    ]
