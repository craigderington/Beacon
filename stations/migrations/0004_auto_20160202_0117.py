# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiostation',
            name='radio_station_frequency',
            field=models.CharField(default=0, help_text='Enter the radio station frequency', max_length=4),
        ),
    ]
