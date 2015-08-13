# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150813_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='public',
            field=models.CharField(default='1', max_length=3, choices=[('1', 'YES'), ('2', 'NO')]),
            preserve_default=True,
        ),
    ]
