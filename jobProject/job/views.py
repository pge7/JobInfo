# -*- coding: utf-8 -*-

#------------------------------------

from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import SearchJobForm
from django.db.models import Q

#from __future__ import unicode_literals
#from django.shortcuts import render
# Create your views here.

def inorCertError():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
# 
def index(request):
    return render(request, 'job/index.html')

def search_job(request):
    title = request.GET.get('title')
    location = request.GET.get('location')
    error_msg=''
    jobs = Job.objects.all()
    if not title or not location:
        error_msg = "Please enter keywords"
        return render(request, 'job/jobquery.html', {'error_msg':error_msg})
    qset = (
            Q(title__icontains = title) &
            Q(location__icontains = location)
            )
    results = Job.objects.filter(qset)
    return render(request, 'job/jobquery.html', {
    'error_msg':error_msg, 'results':results})
