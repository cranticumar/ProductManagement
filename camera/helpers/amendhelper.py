'''
Created on Feb 9, 2016

@author: bkranthi
'''

import os
from django.core.exceptions import ValidationError
from camera.helpers.viewhelper import ViewHelper
from amend.models import Chipset, SoftwareProduct, Geo, Area, SubArea, \
    CaseCount
from amend.interface import LEVELS
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)


class ProductViewHelper(ViewHelper):

    @staticmethod
    def _add_chip(request, context):
        if not (request.POST.get('chip') and request.POST.get('chip_name') and
                request.POST.get('chip_family')):
            raise ValidationError("Please fill all the fields")

        c, created = Chipset.get_or_create(chip_set=request.POST.get('chip'),
                                           chip_name=request.POST.get(
                                               'chip_name'),
                                           chip_family=request.POST.get('chip_family'))

        return ProductViewHelper._return_context(context=context, created=created, msgname='chipform_msg',
                                                 added_data=c.chip)

    @staticmethod
    def _add_sp(request, context):
        if not {'sp', 'chip_select', 'activepl', 'sp_soddate',
                'sp_fcdate', 'sp_csdate'}.issubset(request.POST.keys()):
            raise ValidationError("Please fill all the fields")
        # this below logic will work only for dates in YYYY-MM-DD format
        if not (request.POST.get('sp_soddate') <= request.POST.get('sp_fcdate') <= request.POST.get('sp_csdate')):
            raise ValidationError("Mile stone dates are fake SOD <= FC <= CS")
        sp, created = SoftwareProduct.get_or_create(
            spname=request.POST.get('sp'),
            chip=Chipset.objects.filter(id=request.POST.get('chip_select'))[0],
            active=request.POST.get('activepl'),
            sod_date=request.POST.get('sp_soddate'),
            fc_date=request.POST.get('sp_fcdate'),
            cs_date=request.POST.get('sp_csdate'))
        return ProductViewHelper._return_context(context=context, created=created, msgname='spform_msg',
                                                 added_data=sp.sp_name)

    @staticmethod
    def _add_geo(request, context):
        if not (request.POST.get('geo')):
            raise ValidationError("Invalid Geo")
        geo, created = Geo.get_or_create(location=request.POST.get('geo'))
        return ProductViewHelper._return_context(context=context,
                                                 created=created,
                                                 msgname='geoform_msg',
                                                 added_data=geo.geo)

    @staticmethod
    def _add_areas(request, context):
        if not request.POST.get('area'):
            raise ValidationError("Invalid Area")
        ar, created = Area.get_or_create(area_data=request.POST.get('area'))
        return ProductViewHelper._return_context(context=context,
                                                 created=created,
                                                 msgname='areaform_msg',
                                                 added_data=ar.area)

    @staticmethod
    def _add_subarea(request, context):
        if not (request.POST.get('area_select') and request.POST.get('subarea')):
            raise ValidationError("Invalid Sub Area")
        a = Area.query(ar=request.POST.get('area_select'))
        if a is None:
            raise ValidationError("Are you tracking to hack me??!!")
        sa, created = SubArea.get_or_create(
            fa=a, subarea_data=request.POST.get('subarea'))
        return ProductViewHelper._return_context(context=context,
                                                 created=created,
                                                 msgname='subareaform_msg',
                                                 added_data=sa.subarea)

    @staticmethod
    def _add_trends(request, context):
        if not (request.POST.get('sp_select') and request.POST.get('area_select')):
            raise ValidationError("Please fill all the fields carefully")
        created = False
        return ProductViewHelper._return_context(context=context,
                                                 created=created,
                                                 msgname='trendform_msg',
                                                 added_data='Trends')

    @staticmethod
    def _freeze_counts(request, context):
        if not (request.POST.get('sp_select') and request.POST.get('area_select')):
            raise ValidationError("Please fill all the fields carefully")

        a = Area.query(ar=request.POST.get('area_select'))
        if a is None:
            raise ValidationError("Are you tracking to hack me??!!")

        sp = SoftwareProduct.query(sp_id=request.POST.get('sp_select'))
        if sp is None:
            raise ValidationError("Invalid SP")

        sa = SubArea.query(fa_obj=a)
        if sa is None:
            raise ValidationError("No Sub Areas found under this Area")

        locs = Geo.objects.all()
        for lev in LEVELS:
            lev = str(lev.value)
            for s in sa:
                for l in locs:
                    k = s.subarea + "_" + l.geo + "_L" + str(lev)
                    if k in request.POST.keys():
                        cnt = request.POST.get(k)
                        if cnt == "":
                            cnt = 0
                        cc, created = CaseCount.get_or_create(
                            sp_obj=sp[0], sa_obj=s, lev=lev,
                            loc=l, cnt=cnt)
                        logger.info(cc)

        return ProductViewHelper._return_context(context=context,
                                                 created=created,
                                                 msgname='countsform_msg',
                                                 added_data=a.area + ' counts')

    @staticmethod
    def _return_context(context, created, msgname, added_data):
        if not created:
            context.setdefault(msgname, added_data + " already exists")
        else:
            context.setdefault(msgname, added_data + " added")
        return context
