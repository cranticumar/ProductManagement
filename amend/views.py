# from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Chipset, SoftwareProduct
from django.shortcuts import render
from django.db.utils import IntegrityError
from collections import OrderedDict
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
        context = _load_data_for_forms(context)
    elif request.POST.get('chip_submit') == 'Chip It':
        context.setdefault('loadform', 'chip')
        try:
            context = _add_chip(request, context)
        except IntegrityError:
            context.setdefault('chipform_msg', 'Chip Already Exists')
    elif request.POST.get('sp_submit') == 'Add SP':
        pass
    elif request.POST.get('area_submit') == 'Add Area':
        pass
    elif request.POST.get('default_areas') == 'Insert Default Areas':
        pass
    elif request.POST.get('geo_submit') == 'Insert Geo':
        pass
    elif request.POST.get('trend_submit') == "Insert Trends":
        pass
    elif request.POST.get('count_submit') == "Freeze Counts":
        context.setdefault('loadform', 'counts')
        context = _load_data_for_forms(context)
    return render(request, 'amend/product.html', context)


def _load_data_for_forms(context):
    if context['loadform'] == 'sp':
        chipsets = Chipset.objects.all()
        context.setdefault('chipsets', chipsets)
    elif context['loadform'] in ['counts', 'trends', 'area']:
        sps = SoftwareProduct.objects.all()
        context.setdefault('sps', sps)

    return context


def _add_chip(request, context):
    c = Chipset(chip=request.POST.get('chip'), name=request.POST.get(
        'chip_name'), family=request.POST.get('chip_family'))
    c.save()
    context.setdefault('chipform_msg', c.chip + " chip is in")
    return context


def _add_sp(request, context):
    pass


def _add_geo(request, context):
    pass


def _add_areas(request, context):
    pass


def _add_subareas(request, context):
    pass


def _add_trends(request, context):
    pass


def _freeze_counts(request, context):
    pass
