from django.contrib import admin
from radio.models import Radio, Channel
# Register your models here.

class RadioStack(admin.StackedInline):
    model = Channel
    fk_name = 'radio_channel'
    extra = 1

class RadioAdmin(admin.ModelAdmin):
    fields = (
        'radio_account_id',
        'radio_id',
        'radio_name',
        'radio_model',
        'radio_freq',
    )
    list_display = (
        'radio_account_id',
        'radio_id',
        'radio_name',
        'radio_model',
        'radio_freq',
    )

    search_fields = ['radio_id', 'radio_name', 'radio_model']
    inlines = (RadioStack,)

    class Meta:
        verbose_name = 'Radio'
        verbose_name_plural = 'Radios'


class ChannelAdmin(admin.ModelAdmin):
    fields = (
        'radio_channel',
        'radio_channel_call_sign',
        'radio_channel_slogan',
        'radio_channel_address1',
        'radio_channel_address2',
        'radio_channel_city',
        'radio_channel_state',
        'radio_channel_zip_code',
    )
    list_display = (
        'radio_channel',
        'radio_channel_call_sign',
        'radio_channel_slogan',
        'radio_channel_address1',
        'radio_channel_address2',
        'radio_channel_city',
        'radio_channel_state',
        'radio_channel_zip_code',
    )

    search_fields = ['radio_channel', 'radio_channel_state', 'radio_channel_call_sign']

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'
        ordering = ['-radio_channel_call_sign']

admin.site.register(Radio, RadioAdmin)
admin.site.register(Channel, ChannelAdmin)
