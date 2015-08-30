# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0024_auto_20150830_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 6, 47, 2, 670108)),
        ),
        migrations.AlterField(
            model_name='module',
            name='location',
            field=models.ForeignKey(to='profiles.Partner'),
        ),
    ]
