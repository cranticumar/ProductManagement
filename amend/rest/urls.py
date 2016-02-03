'''
Created on Jan 30, 2016

@author: bkranthi
'''
from django.conf.urls import include, url
from amend.rest.views import ChipsetViewSet, SoftwareProductViewSet
from rest_framework import routers

views = {
    'chipsets': ChipsetViewSet,
    'softwareproducts': SoftwareProductViewSet
}

router = routers.DefaultRouter()
for prefix, view in views.iteritems():
    router.register(prefix, view, prefix)

urlpatterns = [
    url(r'^', include(router.urls))
]