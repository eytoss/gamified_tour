# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-09-16 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(blank=True, default=uuid.uuid4, help_text='Unique, externally-friendly identifier for position', max_length=36, unique=True)),
                ('create_dt', models.DateTimeField(auto_now=True)),
                ('position_x', models.DecimalField(decimal_places=4, help_text="horizontal axis value in current location's coordinate system", max_digits=6)),
                ('position_y', models.DecimalField(decimal_places=4, help_text="vertical axis value in current location's coordinate system", max_digits=6)),
                ('position_orientation', models.DecimalField(blank=True, decimal_places=4, help_text="user's facing direction, for example facing north takes value '0', facing southwest takes value '225'.", max_digits=6, null=True)),
                ('position_accuracy', models.CharField(help_text='confidence level of the position_[x|y|orientation] values', max_length=20)),
            ],
        ),
    ]