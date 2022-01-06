from django.contrib import admin

from .models import FacilityType, List, Facility


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'verbose_name')


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'type',
        'address',
        'full_address',
        'update_date',
        'created_date',
        'cost',
        'stamp',
    )
