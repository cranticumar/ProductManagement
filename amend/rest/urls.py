'''
Created on Jan 30, 2016

@author: bkranthi
'''
from django.conf.urls import include, url
from amend.rest.views import ChipsetViewSet, SoftwareProductViewSet, \
    AreaViewSet, SubAreaViewSet, GeoAreaViewSet, CaseCountViewSet
from rest_framework import routers

views = {
    'chipsets': ChipsetViewSet,
    'softwareproducts': SoftwareProductViewSet,
    'areas': AreaViewSet,
    'subareas': SubAreaViewSet,
    'locations': GeoAreaViewSet,
    'casecounts': CaseCountViewSet
}

router = routers.DefaultRouter()
for prefix, view in views.iteritems():
    router.register(prefix, view, prefix)

urlpatterns = [
    url(r'^', include(router.urls))
]
