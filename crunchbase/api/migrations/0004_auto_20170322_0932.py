# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170322_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people_crunchbase',
            old_name='company',
            new_name='company_name',
        ),
    ]
