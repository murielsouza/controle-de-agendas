# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20170925_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convite',
            name='aceite',
            field=models.BooleanField(default=0),
        ),
    ]
