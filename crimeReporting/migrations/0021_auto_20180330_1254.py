# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-30 07:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crimeReporting', '0020_auto_20180330_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime_timeline',
            name='TIME_OF_UPDATE',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 30, 7, 24, 0, 719898, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='COMPLAINT_DATE',
            field=models.DateField(default=datetime.datetime(2018, 3, 30, 7, 24, 0, 716898, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='COMPLAINT_TIME',
            field=models.TimeField(default=datetime.datetime(2018, 3, 30, 7, 24, 0, 716898, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='information_filing_app',
            name='police_name',
            field=models.ForeignKey(db_column='NAME', on_delete=django.db.models.deletion.CASCADE, to='crimeReporting.USER'),
        ),
    ]
