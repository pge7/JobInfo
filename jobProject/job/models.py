# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=500)
    location = models.CharField(max_length = 250)
    date = models.IntegerField()
    summary = models.CharField(max_length = 1000)
    