# -*- coding: utf-8 -*-

#------------------------------------

from django.shortcuts import render, get_object_or_404
from .models import Job
#from __future__ import unicode_literals
#from django.shortcuts import render
# Create your views here.

def inorCertError():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    

def index(request):
    all_job = Job.objects.all()
    return render(request, 'job/index.html')