# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibutestportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiinfo',
            name='request_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
