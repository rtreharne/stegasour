# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150830_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='pic',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'researcher_images', blank=True),
        ),
    ]
