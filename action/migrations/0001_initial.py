# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-09-16 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(blank=True, default=uuid.uuid4, help_text='Unique, externally-friendly identifier for action', max_length=36, unique=True)),
                ('create_dt', models.DateTimeField(auto_now=True)),
                ('details', models.CharField(help_text='indicate action type, # TODO: will improve this field', max_length=20)),
            ],
        ),
    ]