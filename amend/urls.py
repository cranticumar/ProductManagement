'''
Created on Jan 2, 2016

@author: bkranthi
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$', views.product, name='amendproduct'),
    url(r'^product/(?P<loadform>[a-z]+)/$', views.product, name='amendproduct')
]
