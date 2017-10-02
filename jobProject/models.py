# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse


from scrapy_djangoitem import DjangoItem


class Job(models.Model):
    title = models.CharField(max_length=250, default='no name')
    location = models.CharField(max_length=250, default='no name')
    summary = models.CharField(max_length=1000, default='no name')
    joburl = models.CharField(max_length=3000, default='no name')
    company = models.CharField(max_length=250, default = 'no name')
    #curl = models.CharField(max_length=2000, default='www.indeed.com')
    date = models.CharField(max_length=250, default="no name", blank = True)
    
    
    # class Meta:
        # unique_together=('company', 'title')
    #def get_absolute_url(self):
       # return reverse('MyProjects:index', kwargs={'pk':self.pk})

    
    def __str__(self):
        return self.title

        
class JobItem(DjangoItem):
    django_model = Job