'''
Created on Feb 10, 2016

@author: bkranthi
'''
from amend.models import Chipset, SoftwareProduct, Geo, Area, SubArea


class ViewHelper(object):

    @staticmethod
    def _load_data_for_forms(context, get=None):
        if get is None:
            get = context.get('loadform')

        if get == 'sp':
            chipsets = Chipset.objects.all()
            context.setdefault('chipsets', chipsets)

        if get in ['counts', 'trends', 'area', 'kpi', 'sps']:
            sps = SoftwareProduct.objects.all()
            context.setdefault('sps', sps)

        if get in ['kpi']:
            mps = ['21MP', '16MP', '13MP']
            context.setdefault('mps', mps)

        if get in ['subarea', 'trends', 'counts', 'areas']:
            areas = Area.objects.all()
            context.setdefault('areas', areas)

        if get == 'counts':
            subareas = SubArea.objects.all()
            context.setdefault('subareas', subareas)

        if get == 'counts':
            locs = Geo.objects.all()
            context.setdefault('geos', locs)

        return context

    @staticmethod
    def _query_by_spid(sp_id):
        sp = SoftwareProduct.query(sp_id=sp_id)
        if sp is None:
            return None

        return sp[0]
