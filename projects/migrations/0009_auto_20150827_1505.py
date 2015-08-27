# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_upload_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cohort',
            field=models.ForeignKey(blank=True, to='projects.Cohort', null=True),
        ),
    ]
