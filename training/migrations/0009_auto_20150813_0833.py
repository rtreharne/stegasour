# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_auto_20150813_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 8, 33, 1, 889904)),
        ),
    ]
