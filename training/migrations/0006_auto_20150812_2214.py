# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20150812_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='points',
            field=models.IntegerField(default=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 22, 14, 25, 148495)),
        ),
    ]
