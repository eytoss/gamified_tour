# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-09-17 03:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0002_auto_20170917_0320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modernmodel',
            old_name='update_dt',
            new_name='modify_dt',
        ),
    ]
