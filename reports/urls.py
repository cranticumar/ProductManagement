'''
Created on Feb 10, 2016

@author: bkranthi
'''
from django.conf.urls import url
from reports import views


urlpatterns = [
    url(r'^reportsby/$', views.reportsBy, name='reportsby'),
    url(r'^reportsby/(?P<loadpage>[a-z]+)/$',
        views.reportsBy, name='reportsby'),
    url(r'^reportsby/(?P<loadpage>[a-z]+)/(?P<sp_select>[a-z]+)/(?P<area_select>[a-z]+)/$',
        views.reportsBy, name='reportsby')
]
