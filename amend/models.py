from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from camera.customfields import CustomCaseCharField
from django.contrib.postgres.fields import JSONField
from camera.helpers.modelhelper import ModelHelper
from amend.interface import LEVELS
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)


class Chipset(models.Model):
    '''
    '''
    chip = CustomCaseCharField(char_case='upper', max_length=32, unique=True)
    name = CustomCaseCharField(char_case='title', max_length=32, blank=False)
    family = CustomCaseCharField(char_case='title', max_length=32, blank=False)

    @staticmethod
    def get_or_create(chip_set, chip_name, chip_family):
        """
        Return the existing or new Chipset object given the fields.
        """
        try:
            chipset = Chipset.objects.filter(
                chip=chip_set, name=chip_name, family=chip_family)[0]
            created = False
        except:
            chipset = Chipset.objects.create(
                chip=chip_set, name=chip_name, family=chip_family)
            created = True

        return chipset, created


class SoftwareProduct(models.Model):
    '''
    '''
    sp_name = CustomCaseCharField(
        char_case='upper', max_length=64, verbose_name="SP Name", unique=True)
    chipset = models.ForeignKey(
        Chipset, on_delete=models.PROTECT, related_name="sp_chip")
    active = models.BooleanField(default=True)
    sod_date = models.DateField(default=timezone.now, verbose_name="SOD")
    fc_date = models.DateField(default=timezone.now, verbose_name="FC")
    cs_date = models.DateField(default=timezone.now, verbose_name="CS")

    @staticmethod
    def get_or_create(spname, chip, active, sod_date, fc_date, cs_date):
        """
        Return the existing or new Software Product object given the fields.
        """
        try:
            sp = SoftwareProduct.objects.filter(sp_name=spname)[0]
            created = False
        except:
            sp = SoftwareProduct.objects.create(
                sp_name=spname, chipset=chip, active=active, sod_date=sod_date, fc_date=fc_date, cs_date=cs_date)
            created = True

        return sp, created

    @staticmethod
    def query(sp_id=None, spname=None, chip_obj=None):
        """
        Return the existing Software Product object given any field
        or combination of fields 
        """
        try:
            sp = SoftwareProduct.objects.filter(
                models.Q(id=sp_id) |
                models.Q(sp_name=spname) |
                models.Q(chipset=chip_obj))
            assert(sp)
        except:
            sp = None

        return sp


class Area(models.Model):
    '''
    '''
    area = CustomCaseCharField(
        char_case='title', max_length=64, verbose_name="Area", unique=True, blank=False)

    @staticmethod
    def get_or_create(area_data):
        """
        Return the existing or new Area object given the fields.
        """
        try:
            a = Area.objects.filter(area=area_data)[0]
            created = False
        except:
            a = Area.objects.create(area=area_data)
            created = True

        return a, created

    @staticmethod
    def query(area_id=None, ar=None):
        """
        Return the existing Area object given any field
        or combination fields 
        """
        try:
            a = Area.objects.filter(
                models.Q(id=area_id) | models.Q(area=ar))[0]
        except:
            a = None

        return a


class SubArea(models.Model):
    '''
    '''
    feature_area = models.ForeignKey(
        Area, on_delete=models.PROTECT, related_name="subarea_fa")
    subarea = CustomCaseCharField(
        char_case='upper', max_length=64, verbose_name="Sub Area", blank=False)

    @staticmethod
    def get_or_create(fa, subarea_data):
        """
        Return the existing or new Sub Area object given the fields.
        """
        try:
            sa = SubArea.objects.filter(
                feature_area=fa, subarea=subarea_data)[0]
            created = False
        except:
            sa = SubArea.objects.create(feature_area=fa, subarea=subarea_data)
            created = True

        return sa, created

    @staticmethod
    def query(sa_id=None, fa_obj=None, suba=None):
        """
        Return the existing Sub Area object given any field
        or combination fields 
        """
        try:
            sa = SubArea.objects.filter(
                models.Q(feature_area=fa_obj) |
                models.Q(id=sa_id) |
                models.Q(subarea=suba))
            assert(sa)
        except:
            sa = None

        return sa


class Geo(models.Model):
    '''
    '''
    geo = CustomCaseCharField(
        char_case='upper', max_length=64, verbose_name="Location", unique=True, blank=False)

    @staticmethod
    def get_or_create(location):
        """
        Return the existing or new Geo object given the fields.
        """
        try:
            g = Geo.objects.filter(geo=location)[0]
            created = False
        except:
            g = Geo.objects.create(geo=location)
            created = True

        return g, created


class Trend(models.Model):
    '''
    '''
    sp = models.ForeignKey(
        SoftwareProduct, on_delete=models.PROTECT, related_name="trend_sp")
    feature_area = models.ForeignKey(
        Area, on_delete=models.PROTECT, related_name="trend_fa")
    ps_trend = JSONField(blank=False)
    fc_trend = JSONField(blank=False)
    cs_trend = JSONField(blank=False)

    @staticmethod
    def get_or_create(sp_obj, fa, pst, fct, cst):
        """
        Return the existing or new Trend object given the fields.
        """
        try:
            t = Trend.objects.filter(
                sp=sp_obj, feature_area=fa)[0]
            created = False
        except:
            t = Trend.objects.create(
                sp=sp_obj, feature_area=fa, ps_trend=pst, fc_trend=fct, cs_trend=cst)
            created = True

        return t, created


class CaseCount(models.Model):
    '''
    '''
    softpro = models.ForeignKey(SoftwareProduct,
                                on_delete=models.PROTECT, related_name="cc_sp", verbose_name="SP")
    sub_area = models.ForeignKey(SubArea,
                                 on_delete=models.PROTECT, related_name="cc_subarea", verbose_name="Area-SubArea")
    level = models.CharField(verbose_name="Level",
                             choices=ModelHelper.enum_to_choices(LEVELS), max_length=3)
    location = models.ForeignKey(Geo, verbose_name="Location",
                                 on_delete=models.PROTECT, related_name="cc_geo")
    count = models.IntegerField(blank=False, verbose_name="Count")

    @staticmethod
    def get_or_create(sp_obj, sa_obj, lev, loc, cnt):
        """
        Return the existing or new Case Counts object given the fields.
        """
        try:
            cc = CaseCount.objects.filter(
                softpro=sp_obj, sub_area=sa_obj, level=lev, location=loc)[0]
            created = False
        except:
            cc = CaseCount.objects.create(
                softpro=sp_obj, sub_area=sa_obj, level=lev, location=loc, count=cnt)
            created = True

        return cc, created


class CovPassPercentage(models.Model):
    '''
    '''
    softpro = models.ForeignKey(
        SoftwareProduct, on_delete=models.PROTECT, related_name="cp_sp", blank=False)
    sub_area = models.ForeignKey(
        SubArea, on_delete=models.PROTECT, related_name="cp_subarea", blank=False)
    level = models.CharField(
        choices=ModelHelper.enum_to_choices(LEVELS), max_length=3, blank=False)
    location = models.ForeignKey(
        Geo, on_delete=models.PROTECT, related_name="cp_geo", blank=False)
    tottc = models.IntegerField(blank=False)
    covtc = models.IntegerField(blank=False)
    passtc = models.IntegerField(blank=False)
    failtc = models.IntegerField(blank=False)
    blocktc = models.IntegerField(blank=False)
    na_nr_tc = models.IntegerField(blank=False)
    covper = models.IntegerField(blank=False)
    passper = models.IntegerField(blank=False)
    failper = models.IntegerField(blank=False)
    blockper = models.IntegerField(blank=False)
    time = models.DateTimeField(auto_now_add=True, blank=False)
