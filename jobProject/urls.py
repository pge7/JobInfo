from django.conf.urls import url
from . import views

app_name = 'MyProjects'

urlpatterns = [
   #/MyProjects/detail
    url(r'^detail/', views.detail, name = 'detail'),

   #/MyProjects/index 
    url(r'index/', views.index, name = 'index'),

   #/MyProjects/index/jobquery 
    url(r'jobquery/', views.jobquery, name = 'jobquery'),
    
    url(r'jobsearch_result/',views.search_job, name='jobsearch_result'),
    
    

]
   

