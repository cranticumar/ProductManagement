'''
Created on Jan 30, 2016

@author: bkranthi
'''
from rest_framework import serializers
from amend.models import Chipset, SoftwareProduct, Area, SubArea, Geo, \
    CaseCount


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


class AreaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Area
        fields = ['area']


class SubAreaSerializer(serializers.HyperlinkedModelSerializer):
    feature_area = AreaSerializer()

    class Meta:
        model = SubArea
        fields = ('feature_area', 'subarea')


class GeoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Geo
        fields = ['geo']


class CaseCountSerializer(serializers.HyperlinkedModelSerializer):
    softpro = SoftwareProductSerializer()
    sub_area = SubAreaSerializer()
    location = GeoSerializer()

    class Meta:
        model = CaseCount
        fields = ('softpro', 'sub_area', 'level', 'location', 'count')
