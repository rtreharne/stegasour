# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0012_auto_20150813_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='public',
            field=models.CharField(default='1', max_length=3, choices=[('1', 'YES'), ('2', 'NO')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 9, 31, 10, 616400)),
        ),
    ]
