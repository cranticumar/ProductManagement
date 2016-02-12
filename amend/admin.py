from django.contrib import admin
from amend.models import Chipset, SoftwareProduct, Area, SubArea, Geo, Trend, \
    CaseCount, CovPassPercentage


class ChipsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'chip', 'name', 'family')


class SoftwareProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sp_name', 'chip', 'sod_date', 'fc_date', 'cs_date')

    def chip(self, obj):
        return obj.chipset.chip

    chip.allow_tags = True
    chip.short_description = 'Chipset'


class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'area')


class SubAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fa', 'subarea')

    def fa(self, obj):
        return obj.feature_area.area

    fa.allow_tags = True
    fa.short_description = 'Area'


class GeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'geo')


class CaseCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'sp', 'sa', 'lev', 'location', 'count')

    def sp(self, obj):
        return obj.softpro.sp_name

    def sa(self, obj):
        return obj.sub_area.feature_area.area + "-" + obj.sub_area.subarea

    def lev(self, obj):
        return obj.level

    sp.allow_tags = True
    sa.allow_tags = True


class CovPassPercentageAdmin(CaseCountAdmin):
    list_display = ('sp', 'sa', 'lev', 'location', 'tottc', 'covtc')

# Register your models here.
admin.site.register(Chipset, ChipsetAdmin)
admin.site.register(SoftwareProduct, SoftwareProductAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(SubArea, SubAreaAdmin)
admin.site.register(Geo, GeoAdmin)
admin.site.register(Trend)
admin.site.register(CaseCount, CaseCountAdmin)
admin.site.register(CovPassPercentage, CovPassPercentageAdmin)
