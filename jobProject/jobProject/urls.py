
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Peiyu/', include("AboutMe.urls")),
    url(r'^MyProjects/', include("MyProjects.urls")),
]
