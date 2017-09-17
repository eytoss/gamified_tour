# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-09-17 04:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0004_auto_20170917_0419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modernmodel',
            old_name='id',
            new_name='have_to_do_this_to_make_migration_work',
        ),
        migrations.RemoveField(
            model_name='modernmodel',
            name='create_dt',
        ),
        migrations.RemoveField(
            model_name='modernmodel',
            name='modify_dt',
        ),
        migrations.RemoveField(
            model_name='modernmodel',
            name='meta_data',
        ),
        migrations.RemoveField(
            model_name='modernmodel',
            name='guid',
        ),
        migrations.RemoveField(
            model_name='action',
            name='modernmodel_ptr',
        ),
        migrations.RemoveField(
            model_name='exhibitaction',
            name='modernmodel_ptr',
        ),
        migrations.AddField(
            model_name='action',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 17, 4, 49, 18, 281850, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='action',
            name='guid',
            field=models.CharField(blank=True, default=uuid.uuid4, help_text='Unique, externally-friendly identifier', max_length=36, unique=True),
        ),
        migrations.AddField(
            model_name='action',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='action',
            name='meta_data',
            field=models.CharField(blank=True, help_text='All other available info of this record. Served as 1. Notes. OR 2. Extra info to support backfill should new fields are needed from here.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='modify_dt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='exhibitaction',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 17, 4, 49, 30, 281392, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibitaction',
            name='guid',
            field=models.CharField(blank=True, default=uuid.uuid4, help_text='Unique, externally-friendly identifier', max_length=36, unique=True),
        ),
        migrations.AddField(
            model_name='exhibitaction',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibitaction',
            name='meta_data',
            field=models.CharField(blank=True, help_text='All other available info of this record. Served as 1. Notes. OR 2. Extra info to support backfill should new fields are needed from here.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='exhibitaction',
            name='modify_dt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='ModernModel',
        ),
    ]
