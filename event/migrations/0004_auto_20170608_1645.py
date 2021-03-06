# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20170526_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='banner_1_event',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='banner_2_event',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='banner_3_event',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='logo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
