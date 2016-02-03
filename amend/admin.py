from django.contrib import admin
from amend.models import Chipset, SoftwareProduct, Area, SubArea, Geo, Trend, CaseCount


class ChipsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'chip', 'name', 'family')


class SoftwareProductAdmin(admin.ModelAdmin):
    list_diplay = (
        'id', 'sp_name', 'chipset', 'active', 'sod_date', 'fc_date', 'cs_date')

# Register your models here.
admin.site.register(Chipset, ChipsetAdmin)
admin.site.register(SoftwareProduct, SoftwareProductAdmin)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Geo)
admin.site.register(Trend)
admin.site.register(CaseCount)
