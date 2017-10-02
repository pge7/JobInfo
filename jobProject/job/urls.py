from django.conf.urls import url
from . import views

urlpatterns = [
    #/job/
    url(r'^$', views.index, name='index'),
    url(r'^jobquery/', views.jobquery, name='jobquery'),
]
