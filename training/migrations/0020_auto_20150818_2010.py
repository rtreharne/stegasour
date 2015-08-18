# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0019_auto_20150813_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 20, 10, 14, 688356)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='score',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=1, blank=True),
        ),
    ]
