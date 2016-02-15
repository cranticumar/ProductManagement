'''
Created on Feb 13, 2016

@author: bkranthi
'''
import django_filters
from amend.models import CaseCount


class CaseCountFilter(django_filters.FilterSet):
    '''
    '''
    sp_name = django_filters.CharFilter(name='softpro__sp_name')
    sp_id = django_filters.NumberFilter(name='softpro__id')
    area = django_filters.CharFilter(name='sub_area__feature_area__area')
    subarea = django_filters.CharFilter(name='sub_area__subarea')
    level = django_filters.NumberFilter(name='level')
    geo = django_filters.CharFilter(name='location__geo')

    class Meta:
        model = CaseCount
        fields = ['sp_name', 'sp_id', 'area', 'subarea', 'level', 'geo']
