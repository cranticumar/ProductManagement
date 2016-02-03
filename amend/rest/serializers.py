'''
Created on Jan 30, 2016

@author: bkranthi
'''
from rest_framework import serializers
from amend.models import Chipset, SoftwareProduct


class ChipsetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chipset
        fields = ('chip', 'name', 'family')


class SoftwareProductSerializer(serializers.HyperlinkedModelSerializer):
    chipset = ChipsetSerializer()

    class Meta:
        model = SoftwareProduct
        fields = (
            'sp_name', 'chipset', 'active', 'sod_date', 'fc_date', 'cs_date')
