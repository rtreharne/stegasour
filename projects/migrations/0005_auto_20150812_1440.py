# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150812_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cohort',
            field=models.ForeignKey(to='projects.Cohort'),
        ),
    ]
