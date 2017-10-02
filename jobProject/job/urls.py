from django.conf.urls import url
from . import views

urlpatterns = [
    #/job/
    url(r'^$', views.index, name='index'),
   
    #/job/jobquery 
    url(r'jobquery/', views.jobquery, name = 'jobquery'),
    
    #/job/jobsearch_result 
    url(r'jobsearch_result/',views.search_job, name='jobsearch_result'),
    
]
