# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='supervisor2',
            field=models.ForeignKey(related_name=b'supervisor2', to='profiles.Academic'),
        ),
    ]
