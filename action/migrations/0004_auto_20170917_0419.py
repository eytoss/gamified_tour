# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-09-17 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0003_auto_20170917_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitaction',
            name='create_dt',
        ),
        migrations.RemoveField(
            model_name='exhibitaction',
            name='guid',
        ),
        migrations.RemoveField(
            model_name='exhibitaction',
            name='id',
        ),
        migrations.AddField(
            model_name='exhibitaction',
            name='modernmodel_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='action.ModernModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modernmodel',
            name='meta_data',
            field=models.CharField(blank=True, help_text='All other available info of this record. Served as 1. Notes. OR 2. Extra info to support backfill should new fields are needed from here.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='modernmodel',
            name='modify_dt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]