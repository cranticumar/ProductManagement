from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from camera.customfields import CustomCaseCharField
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Chipset(models.Model):
    '''
    '''
    chip = CustomCaseCharField(char_case='upper', max_length=32, unique=True)
    name = CustomCaseCharField(char_case='title', max_length=32)
    family = CustomCaseCharField(char_case='title', max_length=32)

    def __str__(self):
        return "chip: {c} name: {n} family: {f}".format(
            c=self.chip, n=self.name, f=self.family)


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

#     def __str__(self):
#         return "Software Product: {sp} chipset: {chip} active: {flag} SOD: {sod} FC: {fc} CS: {cs}".format(
# sp=self.sp_name, chip=self.chipset, flag=self.active, sod=self.sod_date,
# fc=self.fc_date, cs=self.cs_date)


class Area(models.Model):
    '''
    '''
    area = CustomCaseCharField(
        char_case='upper', max_length=64, verbose_name="Area", unique=True, blank=False)


class SubArea(models.Model):
    '''
    '''
    feature_area = models.ForeignKey(
        Area, on_delete=models.PROTECT, related_name="subarea_fa")
    subarea = CustomCaseCharField(
        char_case='upper', max_length=64, verbose_name="Sub Area", unique=True, blank=False)


class Geo(models.Model):
    '''
    '''
    geo = CustomCaseCharField(
        char_case='upper', max_length=64, verbose_name="Location", unique=True, blank=False)


class Trend(models.Model):
    '''
    '''
    sp = models.ForeignKey(
        SoftwareProduct, on_delete=models.PROTECT, related_name="trend_sp")
    feature_area = models.ForeignKey(
        Area, on_delete=models.PROTECT, related_name="trend_fa")
    ps_trend = JSONField()
    fc_trend = JSONField()
    cs_trend = JSONField()


class CaseCount(models.Model):
    pass
