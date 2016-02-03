from django.db import models

# Create your models here.
class RadioStation(models.Model):
    AM_BAND = 0
    FM_BAND = 1
    RADIO_BAND = (
        (AM_BAND, 'AM'),
        (FM_BAND, 'FM'),
    )

    radio_station_call_sign = models.CharField(blank=True, max_length=50,
                            help_text="Enter the radio station call sign.")
    radio_station_band = models.PositiveIntegerField(default=0,
                            choices=RADIO_BAND)
    radio_station_frequency = models.CharField(default=0, max_length=5,
                            help_text="Enter the radio station frequency")
    city_of_license = models.CharField(blank=True, max_length=50,
                            help_text="Enter the city of license")
    radio_station_licensee = models.CharField(blank=True, max_length=50,
                            help_text="Enter the radio station licensee.")
    radio_station_format = models.CharField(blank=True, max_length=50,
                            help_text="Enter the station format.")

    def __str__(self):
        return self.radio_station_call_sign


class Office(models.Model):
    radio_station_id = models.ForeignKey('RadioStation')
    office_number = models.CharField(blank=True, max_length=50,
                      help_text='Enter the office ID')
    office_address1 = models.CharField(blank=True, max_length=50,
                      help_text='Enter the office address')
    office_address2 = models.CharField(blank=True, max_length=50,
                      help_text='Enter the office address')
    office_city = models.CharField(blank=True, max_length=50,
                      help_text='Enter the office address')
    office_state = models.CharField(blank=True, max_length=2,
                      help_text='Enter the office address')
    office_postal_code = models.CharField(blank=True, max_length=10,
                      help_text='Enter the office address')
    office_phone = models.CharField(blank=True, max_length=50,
                      help_text='Enter the office address')
    office_fax_number = models.CharField(blank=True, max_length=50,
                      help_text='Enter the office address')

    def __str__(self):
        return self.office_number
