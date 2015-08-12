# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150812_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='attachment',
            field=models.FileField(null=True, upload_to=b'projects', blank=True),
            preserve_default=True,
        ),
    ]
