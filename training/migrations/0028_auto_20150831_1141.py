# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0027_auto_20150831_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 11, 41, 48, 860413)),
        ),
        migrations.AlterField(
            model_name='resource',
            name='embed',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
