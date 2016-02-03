'''
Created on Jan 30, 2016

@author: bkranthi
'''
from rest_framework import viewsets
from amend.models import Chipset, SoftwareProduct
from .serializers import ChipsetSerializer, SoftwareProductSerializer


class ChipsetViewSet(viewsets.ModelViewSet):
    queryset = Chipset.objects.all()
    serializer_class = ChipsetSerializer


class SoftwareProductViewSet(viewsets.ModelViewSet):
    queryset = SoftwareProduct.objects.all()
    serializer_class = SoftwareProductSerializer
