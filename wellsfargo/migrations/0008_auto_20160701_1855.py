# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0007_auto_20160701_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financingplanbenefit',
            old_name='name',
            new_name='group_name',
        ),
    ]