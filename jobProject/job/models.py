# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=500, default='no name')
    location = models.CharField(max_length = 250, default='no name')
    date = models.CharField(max_length =200, default='no name')
    summary = models.CharField(max_length = 1000, default='no name')
    joburl = models.CharField(max_length=3000, default='no name')
