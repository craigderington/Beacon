# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 01:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20160202_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_number', models.CharField(blank=True, help_text='Enter the office ID', max_length=50)),
                ('office_address1', models.CharField(blank=True, help_text='Enter the office address', max_length=50)),
                ('office_address2', models.CharField(blank=True, help_text='Enter the office address', max_length=50)),
                ('office_city', models.CharField(blank=True, help_text='Enter the office address', max_length=50)),
                ('office_state', models.CharField(blank=True, help_text='Enter the office address', max_length=2)),
                ('office_postal_code', models.CharField(blank=True, help_text='Enter the office address', max_length=10)),
                ('office_phone', models.CharField(blank=True, help_text='Enter the office address', max_length=50)),
                ('office_fax_number', models.CharField(blank=True, help_text='Enter the office address', max_length=50)),
                ('radio_station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.RadioStation')),
            ],
        ),
    ]
