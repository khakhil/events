# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170608_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='event_id',
            new_name='event',
        ),
    ]