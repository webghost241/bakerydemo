# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_footertext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footertext',
            options={'verbose_name_plural': 'Footer Text'},
        ),
    ]
