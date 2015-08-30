# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0022_auto_20150827_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='finish',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 6, 2, 22, 845755)),
        ),
    ]
