# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-09-17 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20170917_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(blank=True, default=uuid.uuid4, help_text='Unique, externally-friendly identifier', max_length=36, unique=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('modify_dt', models.DateTimeField(auto_now=True, null=True)),
                ('meta_data', models.CharField(blank=True, help_text='All other available info of this record. Served as 1. Notes. OR 2. Extra info to support backfill should new fields are needed from here.', max_length=200, null=True)),
                ('position_x', models.DecimalField(decimal_places=6, help_text="horizontal axis value in current location's coordinate system", max_digits=10)),
                ('position_y', models.DecimalField(decimal_places=6, help_text="vertical axis value in current location's coordinate system", max_digits=10)),
                ('position_orientation', models.DecimalField(blank=True, decimal_places=6, help_text="entity's facing direction, for example facing north takes value '0', facing southwest takes value '225'.", max_digits=10, null=True)),
                ('position_accuracy', models.CharField(help_text='confidence level of the position_[x|y|orientation] values', max_length=30)),
                ('visible_range', models.DecimalField(blank=True, decimal_places=6, help_text='exhibit will be considered visible in the circle using position as circle point and visible range as radius.', max_digits=10)),
                ('location_id', models.CharField(help_text='need to use FK once location model is built', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Position',
            new_name='UserPosition',
        ),
    ]
