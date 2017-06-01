### ADD THIS FILE IN 

from django.conf.urls import url
from . import views
#### beginning ####
urlpatterns = [url(r'^$', views.index, name='index')]

