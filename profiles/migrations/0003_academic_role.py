# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150812_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic',
            name='role',
            field=models.CharField(default='Academic Manager', max_length=50),
            preserve_default=False,
        ),
    ]
