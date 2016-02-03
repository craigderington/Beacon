from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Radio(models.Model):
    radio_account_id = models.ForeignKey(User)
    radio_id  = models.CharField(max_length=50)
    radio_name = models.CharField(max_length=50)
    radio_model = models.CharField(max_length=50)
    radio_freq = models.CharField(max_length=10)

    def __str__(self):
        return self.radio_name + ' ' + self.radio_id

class Channel(models.Model):
    radio_channel = models.ForeignKey(Radio)
    radio_channel_call_sign = models.CharField(max_length=20)
    radio_channel_slogan = models.CharField(max_length=50)
    radio_channel_address1 = models.CharField(max_length=50)
    radio_channel_address2 = models.CharField(max_length=50)
    radio_channel_city = models.CharField(max_length=50)
    radio_channel_state = models.CharField(max_length=2)
    radio_channel_zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.radio_channel_call_sign + ' ' + self.radio_channel_city
