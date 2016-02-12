'''
Created on Feb 11, 2016

@author: bkranthi
'''
from camera.helpers.viewhelper import ViewHelper
from amend.models import SoftwareProduct, Area


class ReportHelper(ViewHelper):

    @staticmethod
    def _get_report_bysp(context, sp, area, msg):
        sp = SoftwareProduct.query(sp_id=sp)
        if not sp is None:
            context[msg] = sp[0].sp_name

        ar = Area.query(ar=area)
        if not ar is None:
            context[msg] += ' ' + ar.area

        return context, sp[0].sp_name, ar.area
