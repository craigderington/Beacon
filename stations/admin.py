from django.contrib import admin
from stations.models import RadioStation, Office
# Register your models here.

class RadioOfficeInline(admin.StackedInline):
    model = Office
    fk_name = 'radio_station_id'
    extra = 1

class RadioStationAdmin(admin.ModelAdmin):
    fields = (
        'radio_station_call_sign',
        'radio_station_band',
        'radio_station_frequency',
        'radio_station_licensee',
        'radio_station_format',
    )
    list_display = (
        'radio_station_call_sign',
        'radio_station_band',
        'radio_station_frequency',
        'radio_station_licensee',
        'radio_station_format',
    )

    search_fields = (
        'radio_station_band',
        'radio_station_call_sign',
        'radio_station_frequency',
        'radio_station_format',
    )
    inlines = (RadioOfficeInline,)

    class Meta:
        verbose_name = 'Radio Station'
        verbose_name_plural = 'Radio Stations'

admin.site.register(RadioStation, RadioStationAdmin)
