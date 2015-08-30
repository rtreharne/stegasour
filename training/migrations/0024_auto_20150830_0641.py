# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150830_0602'),
        ('training', '0023_auto_20150830_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='location',
            field=models.ForeignKey(blank=True, to='profiles.Partner', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 6, 41, 11, 546361)),
        ),
    ]
