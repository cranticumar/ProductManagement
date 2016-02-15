'''
Created on Jan 30, 2016

@author: bkranthi
'''
from rest_framework import viewsets
from amend.models import Chipset, SoftwareProduct, Area, \
    SubArea, Geo, CaseCount
from amend.rest.serializers import ChipsetSerializer, SoftwareProductSerializer, \
    AreaSerializer, SubAreaSerializer, GeoSerializer, CaseCountSerializer
from amend.rest.filters import CaseCountFilter


class ChipsetViewSet(viewsets.ModelViewSet):
    queryset = Chipset.objects.all()
    serializer_class = ChipsetSerializer


class SoftwareProductViewSet(viewsets.ModelViewSet):
    queryset = SoftwareProduct.objects.all()
    serializer_class = SoftwareProductSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class SubAreaViewSet(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer


class GeoAreaViewSet(viewsets.ModelViewSet):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer


class CaseCountViewSet(viewsets.ModelViewSet):
    queryset = CaseCount.objects.all()
    serializer_class = CaseCountSerializer
    filter_class = CaseCountFilter
