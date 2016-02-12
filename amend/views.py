# from django.http import HttpResponse
from __future__ import print_function
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.utils import IntegrityError
from collections import OrderedDict
from django.core.exceptions import ValidationError
from camera.helpers.amendhelper import ProductViewHelper
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
# Create your views here.


def product(request, loadform=None):
    page = reverse('amendproduct')
    context = {
        'page': page,
        'sidemenu': OrderedDict([
            ('Chip Amendment', page + 'chip'),
            ('SP Amendment', page + 'sp'),
            ('Area Amendment', page + 'area'),
            ('Sub Area Amendment', page + 'subarea'),
            ('Geo Amendment', page + 'geo'),
            ('Trends Amendment', page + 'trends'),
            ('Test Case Counts Amendment', page + 'counts')])
    }

    if not loadform is None:
        context.setdefault('loadform', loadform)

    elif request.POST.get('chip_submit') == 'Chip It':
        context.setdefault('loadform', 'chip')
        try:
            context = ProductViewHelper._add_chip(request, context)
        except IntegrityError:
            context.setdefault('chipform_msg', 'Chip Already Exists')
        except ValidationError as e:
            context.setdefault('chipform_msg', e.message)

    elif request.POST.get('sp_submit') == 'Add SP':
        context.setdefault('loadform', 'sp')
        try:
            context = ProductViewHelper._add_sp(request, context)
        except IntegrityError:
            context.setdefault('spform_msg', 'Software Product Already Exists')
        except ValidationError as e:
            context.setdefault('spform_msg', e.message)

    elif request.POST.get('area_submit') == 'Add Area':
        context.setdefault('loadform', 'area')
        try:
            context = ProductViewHelper._add_areas(request, context)
        except IntegrityError:
            context.setdefault('areaform_msg', 'Area Already Exists')
        except ValidationError as e:
            context.setdefault('areaform_msg', e.message)

    elif request.POST.get('default_areas') == 'Insert Default Areas':
        context.setdefault('loadform', 'area')
        context.setdefault('areaform_msg', "No Functionality for now")

    elif request.POST.get('subarea_submit') == 'Add SubArea':
        context.setdefault('loadform', 'subarea')
        try:
            context = ProductViewHelper._add_subarea(request, context)
        except ValidationError as e:
            context.setdefault('subareaform_msg', e.message)

    elif request.POST.get('geo_submit') == 'Insert Geo':
        context.setdefault('loadform', 'geo')
        try:
            context = ProductViewHelper._add_geo(request, context)
        except IntegrityError:
            context.setdefault('geoform_msg', 'Location Already Exists')
        except ValidationError as e:
            context.setdefault('geoform_msg', e.message)

    elif request.POST.get('trend_submit') == "Insert Trends":
        context.setdefault('loadform', 'trends')

    elif request.POST.get('count_submit'):
        context.setdefault('loadform', 'counts')
        btn = request.POST.get('count_submit')
        try:
            if btn == "Freeze Counts":
                context = ProductViewHelper._freeze_counts(request, context)
            elif btn == "Modify Counts":
                pass
            elif btn == "Fetch Counts":
                pass
        except ValidationError as e:
            context.setdefault('countsform_msg', e.message)

    context = ProductViewHelper._load_data_for_forms(context)
    return render(request, 'amend/product.html', context)


def updateTestStatus(request):
    page = reverse('updatetest')
    context = {
        'page': page,
        'sidemenu': {'load': 'hardcode'}
    }

    spn = ProductViewHelper._query_by_spid(sp_id=request.POST.get('sp_select'))
    ar = request.POST.get('area_select')

    if spn:
        context.setdefault('sp_name', spn)

    if ar:
        context.setdefault('area', ar)

    ProductViewHelper._load_data_for_forms(context, get='sps')
    ProductViewHelper._load_data_for_forms(context, get='areas')
    return render(request, 'amend/updateteststatus.html', context)
