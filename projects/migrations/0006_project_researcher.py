# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150812_1453'),
        ('projects', '0005_auto_20150812_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='researcher',
            field=models.OneToOneField(null=True, blank=True, to='profiles.Researcher'),
            preserve_default=True,
        ),
    ]
