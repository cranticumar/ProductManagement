from collections import OrderedDict
from django.shortcuts import render
from django.core.urlresolvers import reverse
from camera.helpers.reporthelper import ReportHelper
from django.http import HttpResponseRedirect
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)

# Create your views here.


def reportsBy(request, loadpage=None, sp_select=None, area_select=None):
    page = reverse('reportsby')
    context = {
        'page': page,
        'sidemenu': OrderedDict([
            ('Reports By SP', page + 'sp'),
            ('Reports By Chip', page + 'chip'),
            ('Reports By CRs', page + 'crs'),
            ('Reports By SRs', page + 'srs')])
    }

    context.setdefault('loadpage', loadpage)
    context.setdefault('sp_select', sp_select)
    context.setdefault('area_select', area_select)

    if loadpage == "sp":
        context = ReportHelper._load_data_for_forms(context, get='sps')
        context = ReportHelper._load_data_for_forms(context, get='areas')
        if request.POST.get('by') == 'Fetch Report':
            context, spn, area = ReportHelper._get_report_bysp(
                context, sp=request.POST.get('sp_select'),
                area=request.POST.get('area_select'), msg='report')
            HttpResponseRedirect("/sp/" + spn + "/" + area)

    elif loadpage == "chip":
        pass

    elif loadpage == "crs":
        pass

    elif loadpage == "srs":
        pass

    elif loadpage is None:
        context = ReportHelper._load_data_for_forms(context, get='sps')

    return render(request, 'reports/reports.html', context)
