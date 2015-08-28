# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150827_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='label',
            field=models.CharField(max_length=500),
        ),
    ]
