# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views import generic
from django.template.response import TemplateResponse
from .models import Job
from .forms import SearchJobForm
from django.db.models import Q

#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from .models import Job/Album


def index(request):
    # album = get_object_or_404()
    #return HttpResponse("Hello")
    return render(request, 'MyProjects/index.html')

def detail(request):
    return render(request, 'MyProjects/detail.html')

def jobquery(request):
    jobs = Job.objects.all()
    return render(request, 'MyProjects/jobquery.html')

def search_job(request):
    title = request.GET.get('title')
    location = request.GET.get('location')
    error_msg=''
    jobs = Job.objects.all()
    if not title or not location:
        error_msg = "Please enter keywords"
        return render(request, 'MyProjects/jobquery.html', {'error_msg':error_msg})
    qset = (
            Q(title__icontains = title) &
            Q(location__icontains = location)
            )
    results = Job.objects.filter(qset)
    return render(request, 'MyProjects/jobquery.html', {
    'error_msg':error_msg, 'results':results})


#class IndexView(generic.ListView)
    #template_name = 'MyProject/index.html'
    #context_object_name = "object_list"
    
    #def get_query(self):
       # return Album.objects.all()

#class DetailView(generic.DetailView):
    # model = Album
     #template_name = 'MyProject/detail.html'

#class DetailView(generic.DetailView):
    # model = Album
     #template_name = 'MyProject/detail.html'

#class JobCreate(CreateView):
    # model = Job
     #fields = ['title','location','date','summary']







